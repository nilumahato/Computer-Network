## Question
Filter a Wireshark capture on IPv6 and explain why its field has the value that it does.

## Answer

### Filtering a Wireshark Capture on IPv6

To filter a Wireshark capture to display only IPv6 traffic, you can use the display filter `ipv6`. This filter will show all packets that contain IPv6 traffic.

### Example Steps to Filter IPv6 Traffic in Wireshark

1. **Open Wireshark**: Launch the Wireshark application on your computer.
2. **Start Capturing Packets**: Click on the network interface you want to capture traffic on and start the capture.
3. **Apply Filter**: Once you have captured some traffic, type `ipv6` in the display filter bar at the top of the Wireshark window and press Enter. This will filter the capture to show only IPv6 packets.

### Explanation of IPv6 Fields

When examining an IPv6 packet in Wireshark, you will see several fields within the IPv6 header. Here is a brief explanation of some key fields and why they have specific values:

1. **Version**: This field will have a value of `6`, indicating that the packet is an IPv6 packet. The value is fixed as it denotes the version of the IP protocol.

2. **Traffic Class**: This field is used for packet prioritization. It can have various values depending on the priority assigned to the packet by the sender.

3. **Flow Label**: This 20-bit field is used to label sequences of packets that require special handling by IPv6 routers, such as real-time service between a pair of hosts. The value is chosen by the sender and can vary based on the requirements of the traffic flow.

4. **Payload Length**: This field specifies the length of the data carried by the IPv6 packet. Its value depends on the size of the payload (i.e., the data being transmitted).

5. **Next Header**: This field identifies the type of header immediately following the IPv6 header. Common values include `6` for TCP, `17` for UDP, and `58` for ICMPv6.

6. **Hop Limit**: Similar to the Time to Live (TTL) field in IPv4, this field specifies the maximum number of hops (routers) the packet can traverse. Each router that forwards the packet decrements this value by one. If the value reaches zero, the packet is discarded.

7. **Source Address**: This field contains the IPv6 address of the sender. The value depends on the address assigned to the sender's network interface.

8. **Destination Address**: This field contains the IPv6 address of the receiver. The value depends on the address to which the packet is being sent.

### Example Packet Analysis

Let's consider an example IPv6 packet:

Internet Protocol Version 6, Src: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, Dst: 2001:0db8:85a3:0000:0000:8a2e:0370:7335
0110 .... = Version: 6
.... 0000 0000 .... = Traffic Class: 0x00
.... .... .... 0000 0000 0000 0000 = Flow Label: 0x00000
Payload Length: 64
Next Header: TCP (6)
Hop Limit: 64
Source: 2001:0db8:85a3::8a2e:370:7334
Destination: 2001:0db8:85a3::8a2e:370:7335

- **Version**: 6 (indicates IPv6)
- **Traffic Class**: 0x00 (default, no special priority)
- **Flow Label**: 0x00000 (default, no special handling)
- **Payload Length**: 64 bytes (length of the payload data)
- **Next Header**: TCP (value 6, indicating the next header is a TCP header)
- **Hop Limit**: 64 (initial value, decremented by each router)
- **Source Address**: 2001:0db8:85a3::8a2e:370:7334 (the sender's IPv6 address)
- **Destination Address**: 2001:0db8:85a3::8a2e:370:7335 (the receiver's IPv6 address)