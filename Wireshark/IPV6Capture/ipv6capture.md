
# Analysis of IPv6 Headers

## Capturing IPv6 Packets in Wireshark
![image](file:///mnt/data/image.png)
We filtered IPv6 packets in Wireshark with the `ipv6` filter.

## Analyzing Headers
### 1. Version
- Version header specifies the IP version. In our case, it's 6 i.e., IPv6.

### 2. Traffic Class
- This field is used to distinguish between different classes or priorities of IPv6 packets.

### 3. Flow Label
- Flow Label is used for labeling packets belonging to the same flow. In our case, it's `0x00000`.

### 4. Payload Length
- This specifies the length of the payload, not including the IPv6 header. Here, the length is 32 bytes.

### 5. Next Header
- Indicates the type of the next header following the IPv6 header. Here, it is `IPv6 Hop-by-Hop Option (0)`, which indicates the presence of additional headers before the actual data.

### 6. Hop Limit
- Similar to the Time to Live (TTL) in IPv4, it specifies the maximum number of hops the packet is allowed before being discarded. Here, the hop limit is 1.

### 7. Source Address
- This is the IPv6 address of the source device: `fe80::e10b:d611:99cc:1307`.

### 8. Destination Address
- This is the IPv6 address of the destination device: `ff02::1:ffce:1307`.

### 9. IPv6 Hop-by-Hop Option
- **Next Header:** ICMPv6 (58)
- **Length:** 8 bytes
- **Router Alert:**
  - **Type:** Router Alert (0x05)
  - **Action:** Skip and continue (0)
  - **May Change:** No
  - **Low-Order Bits:** 0x05
- **PadN:**
  - **Type:** PadN (0x01)
  - **Length:** 0

### 10. Internet Control Message Protocol v6 (ICMPv6)
- **Type:** Multicast Listener Report (131)
- **Code:** 0
- **Checksum:** 0xf684 (correct)
- **Checksum Status:** Good
- **Maximum Response Delay:** 0 ms
- **Reserved:** 0000
- **Multicast Address:** `ff02::1:ffce:1307`

This packet is an ICMPv6 Multicast Listener Report, indicating that the device is reporting its membership in a multicast group.
