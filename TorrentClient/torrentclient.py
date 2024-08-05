import random
import string
import bencodepy
import hashlib
import requests
import struct
import socket
import time

def generate_peer_id():
    return '-GO1000-' + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def read_torrent_file(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()
    return bencodepy.decode(file_content)

def print_tracker_list(torrent_data):
    announce_list = torrent_data.get(b'announce-list')
    if announce_list:
        trackers = [tracker[0].decode('utf-8') for tracker in announce_list]
    else:
        trackers = [torrent_data[b'announce'].decode('utf-8')]
    
    for tracker in trackers:
        print(tracker)

def get_peers_from_tracker(torrent_data, peer_id, port=6881):
    info = torrent_data[b'info']
    info_hash = hashlib.sha1(bencodepy.encode(info)).digest()
    
    announce_url = torrent_data[b'announce'].decode('utf-8')
    
    params = {
        'info_hash': info_hash,
        'peer_id': peer_id.encode('utf-8'),
        'port': port,
        'uploaded': 0,
        'downloaded': 0,
        'left': info.get(b'length', 0),
        'compact': 1
    }

    response = requests.get(announce_url, params=params)
    if response.status_code == 200:
        return bencodepy.decode(response.content)
    else:
        print("Failed to connect to tracker:", response.status_code, response.text)
        return None

def parse_peers(peers):
    peers_list = []
    for i in range(0, len(peers), 6):
        ip = '.'.join(map(str, peers[i:i+4]))
        port = struct.unpack(">H", peers[i+4:i+6])[0]
        peers_list.append((ip, port))
    return peers_list

def handshake(info_hash, peer_id):
    pstrlen = b'\x13'  # 19 in bytes
    pstr = b"BitTorrent protocol"
    reserved = b'\x00' * 8
    return pstrlen + pstr + reserved + info_hash + peer_id.encode('utf-8')

def connect_to_peer(peer, info_hash, peer_id):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # Set a timeout for connections
        print(f"Connecting to peer: {peer}")
        sock.connect(peer)
        sock.send(handshake(info_hash, peer_id))

        # Receive handshake response
        response = sock.recv(68)
        if len(response) != 68:
            print("Handshake failed with peer:", peer)
            return None

        # Check if the received info hash matches
        received_info_hash = response[28:48]
        if received_info_hash != info_hash:
            print("Info hash mismatch with peer:", peer)
            return None

        print("Handshake successful with peer:", peer)
        return sock
    except Exception as e:
        print(f"Connection failed with peer: {peer}, Error: {e}")
        return None

def send_interested(sock):
    interested_msg = struct.pack('>Ib', 1, 2)
    sock.send(interested_msg)

def receive_message(sock):
    try:
        length_prefix = sock.recv(4)
        if not length_prefix:
            return None, None
        length = struct.unpack('>I', length_prefix)[0]
        if length == 0:
            return None, None

        message_id = sock.recv(1)[0]
        payload = sock.recv(length - 1)
        return message_id, payload
    except Exception as e:
        print(f"Error receiving message: {e}")
        return None, None

def request_piece(sock, index, begin, length):
    request_msg = struct.pack('>IbIII', 13, 6, index, begin, length)
    sock.send(request_msg)

def receive_piece(sock):
    try:
        length_prefix = sock.recv(4)
        if len(length_prefix) < 4:
            return None, None, None

        length = struct.unpack('>I', length_prefix)[0]
        if length == 0:
            return None, None, None

        message_id = sock.recv(1)[0]
        if message_id != 7:  # 7 is the message ID for 'piece'
            return None, None, None

        index = struct.unpack('>I', sock.recv(4))[0]
        begin = struct.unpack('>I', sock.recv(4))[0]
        block = sock.recv(length - 9)
        return index, begin, block
    except Exception as e:
        print(f"Error receiving piece: {e}")
        return None, None, None

def send_have(sock, index):
    have_msg = struct.pack('>IbI', 5, 4, index)
    sock.send(have_msg)

# Example usage:
peer_id = generate_peer_id()
torrent_file_path = '/home/patali/development/torrentClient/codecrafters-bittorrent-python/sample.torrent'
torrent_data = read_torrent_file(torrent_file_path)
info = torrent_data[b'info']
info_hash = hashlib.sha1(bencodepy.encode(info)).digest()
total_length = info[b'length']
print("Total length is ", total_length)
pieces_hashes = info[b'pieces']
total_pieces = len(pieces_hashes) // 20 # Each hash is 20 bytes
print_tracker_list(torrent_data)
peers = get_peers_from_tracker(torrent_data, peer_id)
if peers:
    compact_peers = peers[b'peers']
    parsed_peers = parse_peers(compact_peers)

    with open('downloaded_file', 'wb') as f:
        downloaded_length = 0
        piece_number = 0
        block_size = 16384
        block_offset = 0

        while downloaded_length < total_length:
            for peer in parsed_peers:
                sock = connect_to_peer(peer, info_hash, peer_id)
                if sock:
                    send_interested(sock)
                    choked = True

                    while choked:
                        message_id, payload = receive_message(sock)
                        if message_id is None:
                            print("Connection closed by peer")
                            break
                        if message_id == 1:  # unchoke message
                            choked = False
                            print("Received unchoke from peer:", peer)
                            while not choked and downloaded_length < total_length:
                                try:
                                    if piece_number != (total_pieces-1):
                                        print(block_offset, info[b'piece length'])
                                        piece_length = info[b'piece length']
                                        if block_offset < piece_length:
                                            print("Block offset is ", block_offset)
                                            remaining = piece_length - block_offset

                                            request_size = min(block_size, remaining)
                                            print("Request size is ", request_size)

                                            request_piece(sock, piece_number, block_offset, request_size)
                                            index, begin, block = receive_piece(sock)

                                            if block is not None:
                                                f.write(block)
                                                downloaded_length += len(block)
                                                block_offset += len(block)
                                                print(f"Received piece: index={index}, offset={begin}, block length={len(block)}")
                                            else:
                                                break
                                        else:
                                            piece_number += 1
                                            block_offset = 0
                                    else:
                                        piece_length = total_length - downloaded_length
                                        if(piece_length>block_size):
                                            request_piece(sock, piece_number, block_offset, block_size)
                                            index, begin, block = receive_piece(sock)
                                            if block is not None:
                                                f.write(block)
                                                downloaded_length += len(block)
                                                block_offset += len(block)
                                                if(downloaded_length >= total_length):
                                                    break
                                                print(f"Received piece: index={index}, offset={begin}, block length={len(block)}")
                                            else:
                                                print("Failed to receive piece, retrying...")
                                                break
                                        else:
                                            request_piece(sock, piece_number, block_offset, piece_length)
                                            index, begin, block = receive_piece(sock)
                                            if block is not None:
                                                f.write(block)
                                                downloaded_length += len(block)
                                                block_offset += len(block)
                                                print(f"Received piece: index={index}, offset={begin}, block length={len(block)}")
                                            if(downloaded_length >= total_length):
                                                break
                                        
                                except Exception as e:
                                    print(f"Error in download loop: {e}")
                                    break
                    sock.close()

else:
    print("Failed to get peers from tracker")

print(f"Download complete. Total downloaded length: {downloaded_length}/{total_length}")
