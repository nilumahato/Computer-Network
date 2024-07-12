# Using Wireshark to Capture DHCP Packets

## Question:

Use Wireshark to demonstrate different packets involved in getting an IP address from a DHCP server.

## Answer:

### Wireshark Demonstration

#### Objective:

To capture and analyze DHCP (Dynamic Host Configuration Protocol) packets using Wireshark, demonstrating the process of obtaining an IP address from a DHCP server.

#### Equipment Needed:

- **Computer:** Running Wireshark for packet capture.
- **Network Setup:** Includes a DHCP server, a DHCP client (target device), and a network infrastructure.

#### Steps:

1. **Start Wireshark Capture:**

   - Open Wireshark on the computer connected to the network.

2. **Filter DHCP Packets:**

   - Apply a display filter to capture DHCP packets:
     ```
     bootp
     ```

3. **Initiate DHCP Process:**

   - Power on the DHCP client (target device) connected to the network.

4. **Capture DHCP Packets:**

   - Observe the sequence of DHCP packets captured by Wireshark:
     - **DHCP Discover:** Sent by the client to discover available DHCP servers on the network.
     - **DHCP Offer:** Sent by DHCP servers in response to DHCP Discover, offering IP address lease and configuration parameters.
     - **DHCP Request:** Sent by the client to request the offered IP address from a specific DHCP server.
     - **DHCP Acknowledge (DHCPACK):** Sent by the DHCP server to confirm the IP address assignment to the client.

5. **Analysis:**

   - Analyze the captured packets to understand:
     - Source and destination IP addresses.
     - DHCP options exchanged (subnet mask, default gateway, DNS server addresses, lease duration).
     - Timing and sequence of packet exchanges during the DHCP process.

6. **Save Capture File:**

   - Save the Wireshark capture file for future reference and analysis.

#### Example Capture:

- An example of Wireshark capture file name: `DHCP_Packet_Capture_Example.pcapng`

### Conclusion:

Using Wireshark to capture DHCP packets provides insight into the dynamic IP address allocation process. This exercise demonstrates the interaction between DHCP clients and servers, highlighting the role of each packet type in obtaining and configuring IP addresses on a network.

