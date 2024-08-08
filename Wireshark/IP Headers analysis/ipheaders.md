# Analysis of  IP headers

## Capturing IP Packets in Wireshark
![image](https://github.com/user-attachments/assets/6fe9ae4b-29ca-4cdd-9364-e21b997817b9)
We filtered IP packets in wireshark with ```ip``` filter.

## Analysing Headers
### 1. Version
- Version header specifies the IP version. In our case, its 4 i.e IPV4

## 2. Header Length
- This header specifies the length of the IP packet which is 20 Bytes.

## 3. Total Length
- It is the total length of the IPv4 packet, including both the IPv4 header and the payload. It has value 52 Bytes. 

## 4. Identification
- An identifier to help reassemble fragmented packets.

## 5. Flags
- In our case, its 0x40 (Don't Fragment) - Indicates that the packet should not be fragmented.
    - Reserved bit: Not set.
    - Don't Fragment: Set.
    - More Fragments: Not set.

## 6. Fragment Offset
- We have as 0 and it ondicates the position of this fragment in the original packefor non-fragmented packets.

## Time to Live (TTL)
 - It is the value that specifies the number of hops the packet can traverse before being discarded. Here, we have 64.
 
 ## Protocol: TCP
 - It indicates that the next layer protocol is TCP.
 
## Header Checksum: 0x2dcd
 Its used for error-checking the header. Here we have 0x2dcd.
 
## Header checksum status: 
- Unverified (validation is disabled). Its used by each router to figureout if there is any error.

## Source Address 
- Its 192.168.1.87 and it isthe IP address of the source device. 

## Destination Address 
- Its destination IP address and it is 35.190.72.216. 