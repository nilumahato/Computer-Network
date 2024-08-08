# Analysis of  TCP headers

## Capturing TCP Packets in Wireshark

![image](https://github.com/user-attachments/assets/0ad97498-4d10-4b27-87fb-1c768b302446)

We filtered TCP packets in wireshark with ```tcp``` filter.

## Analysing Headers
### Source Port: 45694
Source port header has the value of port number of the source device.  

### Destination Port: 443
This is the port number on the destination device. 

### Stream index: 0
This is an index used to identify the stream of packets. Stream 0 typically means the first conversation in the packet capture.

### Conversation completeness: Incomplete, DATA (15)
This indicates that the entire conversation has not been captured; only 15 segments of data are present.

### TCP Segment Len: 1380
The length of this TCP segment is 1380 bytes.

### Sequence Number: 3769 (relative sequence number)
This is the sequence number of the first byte in this TCP segment, relative to the start of the conversation.

### Sequence Number (raw): 3338006298
The actual sequence number used in the TCP header.

### Next Sequence Number: 5149 (relative sequence number)
The sequence number of the next byte that is expected to be sent, relative to the start of the conversation.

### Acknowledgment Number: 2862 (relative ack number)
This is the acknowledgment number, indicating the next byte the sender expects to receive.

### Acknowledgment number (raw): 1160701906
The actual acknowledgment number used in the TCP header.

### Header Length: 32 bytes (8)
The length of the TCP header is 32 bytes, which is 8 (4-byte) words.

### Flags: 0x010 (ACK)
The flags field in the TCP header, showing that only the ACK (acknowledgment) flag is set.

### Window: 501
The size of the TCP receive window, which is a flow control mechanism.

### Calculated window size: 64128
The actual size of the TCP receive window after applying the window size scaling factor.
### Window size scaling factor: 128
The scaling factor used to calculate the actual window size.

### Checksum: 0x5c16 [unverified]
The checksum for error-checking purposes.

### Checksum Status: Unverified
The status of the checksum, indicating it hasn't been verified.

### Urgent Pointer: 0
This field is used if the URG flag is set, indicating that there is no urgent data in this segment.

### Options: (12 bytes)
The Options field in the TCP header is used to enhance and extend the capabilities of the TCP protocol. This field allows for various optional parameters to be included in the TCP segment, which can provide additional functionalities, improve performance, or support new features. It includes the additional headers like Maximum segment size, SACK permitted, Timestamps, No-Operation (NOP) and Window scale. In our case it has following headers and values. 
   -  TCP Option - Maximum segment size: 1440 bytes
   -  TCP Option - SACK permitted
   -  TCP Option - Timestamps: TSval 2755142522, TSecr 0
   -  TCP Option - No-Operation (NOP)
   -  TCP Option - Window scale: 7 (multiply by 128)

### Timestamps
Timestamps headers has the timestamp of TCP packets. In our case, it has following value: 
   - [Time since first frame in this TCP stream: 0.000000000 seconds]
   -  [Time since previous frame in this TCP stream: 0.000000000 seconds]



