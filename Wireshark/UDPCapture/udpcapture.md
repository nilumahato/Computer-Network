
# Analysis of UDP Headers

## Capturing UDP Packets in Wireshark

![image](https://github.com/user-attachments/assets/35ddc8a0-6efb-4642-934f-f302291cdecb)


We filtered UDP packets in Wireshark with the `udp` filter.

## Analyzing Headers

### Source Port: 2408
The source port header indicates the port number of the source device that sent the packet.

### Destination Port: 57611
This is the port number on the destination device where the packet is being sent.

### Stream index: 0
This is an index used to identify the stream of packets. Stream 0 typically means the first conversation in the packet capture.

### Length: 92
The length of this UDP packet, including both the header and the payload.

### Checksum: 0x3e68 [unverified]
The checksum is used for error-checking purposes. The status "unverified" indicates it hasn't been verified by Wireshark.

### Checksum Status: Unverified
The status of the checksum, indicating it hasn't been verified.

### UDP Payload: 84 bytes
The payload of this UDP packet, which is 84 bytes.

### Timestamps
Timestamp headers provide the timing of UDP packets. In our case, it has the following values:
- **Time since first frame:** 0.000000000 seconds
  - This indicates the time since the first frame in this UDP stream.
- **Time since previous frame:** 0.000000000 seconds
  - This indicates the time since the previous frame in this UDP stream.

### Hex Dump and ASCII Representation
The bottom pane of Wireshark shows the hex dump of the selected UDP packet along with its ASCII representation. This allows for a detailed inspection of the raw packet data, which can be useful for troubleshooting and analysis. 

### Summary
The displayed packets represent a conversation between two IP addresses (`192.168.1.87` and `162.159.192.10`) over UDP, with the source port `2408` and destination port `57611`. The data length of each UDP packet is 84 bytes, and the packets are being captured in real-time as indicated by the timestamps.

If further analysis is needed, such as determining the nature of the payload or identifying any patterns in the communication, we can look into the payload data more closely or apply additional filters in Wireshark.
