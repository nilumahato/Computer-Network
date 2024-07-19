import json
import sys
import bencodepy
import hashlib
import requests
import struct
import socket
import math
import os

bc = bencodepy.Bencode(encoding=None)  # Set encoding to None to handle binary data

def decode_bencode(bencoded_value):
    return bc.decode(bencoded_value)

def bytes_to_str(data):
    if isinstance(data, bytes):
        try:
            return data.decode('utf-8')
        except UnicodeDecodeError:
            return data.hex()  # For binary data that can't be decoded, return hex representation
    elif isinstance(data, dict):
        return {bytes_to_str(k): bytes_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [bytes_to_str(item) for item in data]
    else:
        return data

def get_peers(torrent_info, info_hash):
    tracker_url = torrent_info.get(b"announce", b"").decode("utf-8")
    params = {
        "info_hash": info_hash,
        "peer_id": "00112233445566778899".encode('utf-8'),
        "port": 6881,
        "uploaded": 0,
        "downloaded": 0,
        "left": torrent_info[b"info"].get(b"length", 0),
        "compact": 1,
    }
    response = requests.get(tracker_url, params=params)
    response_dict = decode_bencode(response.content)
    peers = response_dict.get(b"peers", b"")
    peer_list = []
    for i in range(0, len(peers), 6):
        ip = ".".join(str(b) for b in peers[i:i + 4])
        port = struct.unpack("!H", peers[i + 4:i + 6])[0]
        peer_list.append(f"{ip}:{port}")
    return peer_list

def extract_pieces_hashes(pieces):
    return [pieces[i:i + 20] for i in range(0, len(pieces), 20)]



def download(output_file, torrent_file):
    decoded_value = decode_bencode(open(torrent_file, "rb").read())
    total_pieces = len(extract_pieces_hashes(decoded_value[b"info"][b"pieces"]))
    piece_files = []
    
    for piece_index in range(total_pieces):
        piece_path = f"/tmp/test-{piece_index}"
        download_piece(decoded_value, hashlib.sha1(bencodepy.encode(decoded_value[b"info"])).digest(), piece_index, piece_path)
        piece_files.append(piece_path)
    
    with open(output_file, "ab") as result_file:
        for piece_file in piece_files:
            with open(piece_file, "rb") as pf:
                result_file.write(pf.read())
            os.remove(piece_file)

def download_piece(decoded_data, info_hash, piece_index, output_file):
    peers = get_peers(decoded_data, info_hash)
    peer_ip, peer_port = peers[0].split(":")
    peer_port = int(peer_port)
    protocol_name_length = struct.pack(">B", 19)
    protocol_name = b"BitTorrent protocol"
    reserved_bytes = b"\x00" * 8
    peer_id = b"PC0001-7694471987235"
    payload = (
        protocol_name_length + protocol_name + reserved_bytes + info_hash + peer_id
    )
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((peer_ip, peer_port))
        sock.sendall(payload)
        response = sock.recv(68)
        message = receive_message(sock)
        while int(message[4]) != 5:
            message = receive_message(sock)
        interested_payload = struct.pack(">IB", 1, 2)
        sock.sendall(interested_payload)
        message = receive_message(sock)
        while int(message[4]) != 1:
            message = receive_message(sock)
        file_length = decoded_data[b"info"][b"length"]
        total_number_of_pieces = len(
            extract_pieces_hashes(decoded_data[b"info"][b"pieces"])
        )
        default_piece_length = decoded_data[b"info"][b"piece length"]
        if piece_index == total_number_of_pieces - 1:
            piece_length = file_length - (default_piece_length * piece_index)
        else:
            piece_length = default_piece_length
        number_of_blocks = math.ceil(piece_length / (16 * 1024))
        data = bytearray()
        for block_index in range(number_of_blocks):
            begin = 2**14 * block_index
            print(f"begin: {begin}")
            block_length = min(piece_length - begin, 2**14)
            print(
                f"Requesting block {block_index + 1} of {number_of_blocks} with length {block_length}"
            )
            request_payload = struct.pack(
                ">IBIII", 13, 6, piece_index, begin, block_length
            )
            print("Requesting block, with payload:")
            print(request_payload)
            print(struct.unpack(">IBIII", request_payload))
            print(int.from_bytes(request_payload[:4], byteorder='big'))
            print(int.from_bytes(request_payload[4:5], byteorder='big'))
            print(int.from_bytes(request_payload[5:9], byteorder='big'))
            print(int.from_bytes(request_payload[17:21], byteorder='big'))
            sock.sendall(request_payload)
            message = receive_message(sock)
            data.extend(message[13:])
        with open(output_file, "wb") as f:
            f.write(data)
    finally:
        sock.close()
    return True

def receive_message(s):
    length = s.recv(4)
    while not length or not int.from_bytes(length, byteorder='big'):
        length = s.recv(4)
    message = s.recv(int.from_bytes(length, byteorder='big'))
    # If we didn't receive the full message for some reason, keep gobbling.
    while len(message) < int.from_bytes(length, byteorder='big'):
        message += s.recv(int.from_bytes(length, byteorder='big') - len(message))
    return length + message

def main():
    command = sys.argv[1]

    if command == "decode":
        bencoded_value = sys.argv[2].encode()
        decoded_value = decode_bencode(bencoded_value)
        print(json.dumps(bytes_to_str(decoded_value)))
    elif command == "info":
        with open(sys.argv[2], "rb") as f:
            data = f.read()
            print(data)
            parsed = decode_bencode(data)
            tracker_url = parsed.get(b"announce", b"").decode("utf-8")
            print("Tracker URL:", tracker_url)
            length = parsed[b"info"].get(b"length", "Unknown length")
            print("Length:", length)
            name = parsed[b"info"].get(b"name", b"").decode("utf-8")
            info_hash = hashlib.sha1(bencodepy.encode(parsed[b"info"])).hexdigest()
            print("Name:", name)
            piece_length = parsed[b"info"].get(b"piece length", "Unknown piece length")
            print("Piece Length:", piece_length)
            pieces = parsed[b"info"].get(b"pieces", b"").hex()
            print("Pieces (hex):", pieces)
            print(f"Info Hash: {info_hash}")
    elif command == "peers":
        with open(sys.argv[2], "rb") as f:
            bencoded_value = f.read()
        torrent_info = decode_bencode(bencoded_value)
        tracker_url = torrent_info.get(b"announce", b"").decode("utf-8")
        info_dict = torrent_info.get(b"info", {})
        bencoded_info = bencodepy.encode(info_dict)
        info_hash = hashlib.sha1(bencoded_info).digest()
        params = {
            "info_hash": info_hash,
            "peer_id": "00112233445566778899".encode('utf-8'),
            "port": 6881,
            "uploaded": 0,
            "downloaded": 0,
            "left": info_dict.get(b"length", 0),
            "compact": 1,
        }
        response = requests.get(tracker_url, params=params)
        response_dict = decode_bencode(response.content)
        peers = response_dict.get(b"peers", b"")
        for i in range(0, len(peers), 6):
            ip = ".".join(str(b) for b in peers[i:i + 4])
            port = struct.unpack("!H", peers[i + 4:i + 6])[0]
            print(f"Peer: {ip}:{port}")
    elif command == "handshake":
        file_name = sys.argv[2]
        (ip, port) = sys.argv[3].split(":")
        with open(file_name, "rb") as file:
            parsed = decode_bencode(file.read())
            info = parsed[b"info"]
            bencoded_info = bencodepy.encode(info)
            info_hash = hashlib.sha1(bencoded_info).digest()
            handshake = (
                b"\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00"
                + info_hash
                + b"00112233445566778899"
            )
            # make request to peer
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip, int(port)))
                s.send(handshake)
                print(f"Peer ID: {s.recv(68)[48:].hex()}")
    elif command == "download_piece":
        output_file = sys.argv[3]
        piece_index = int(sys.argv[5])
        torrent_file = sys.argv[4]
        with open(torrent_file, "rb") as f:
            torrent_data = f.read()
        decoded_data = decode_bencode(torrent_data)
        if download_piece(
            decoded_data,
            hashlib.sha1(bencodepy.encode(decoded_data[b"info"])).digest(),
            piece_index,
            output_file,
        ):
            print(f"Piece {piece_index} downloaded to {output_file}.")
        else:
            raise RuntimeError("Failed to download piece")
    elif command == "download":
        if len(sys.argv) != 5:
            raise NotImplementedError(
                f"Usage: {sys.argv[0]} download -o output filename"
            )
        outputfile = sys.argv[3]
        filename = sys.argv[4]
        download(outputfile, filename)
        print("Download %s to %s" % (filename, outputfile))
        
    else:
        raise NotImplementedError(f"Unknown command {command}")

if __name__ == "__main__":
    main()
