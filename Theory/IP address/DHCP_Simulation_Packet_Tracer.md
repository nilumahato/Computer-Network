# Simulating DHCP on Packet Tracer with Two Different Networks

## Question:

Simulate DHCP on Packet Tracer. Have at least two different networks.

## Answer:

### Simulation Setup

#### Objective:

To simulate DHCP (Dynamic Host Configuration Protocol) on Cisco Packet Tracer, demonstrating automatic IP address assignment across two different networks.

#### Components:

1. **Devices:**
   - **Router:** Connects the two networks and facilitates inter-network communication.
   - **Switches:** Provide connectivity for devices within each network segment.
   - **PCs:** Represent DHCP clients that request IP addresses dynamically from the DHCP server.

2. **DHCP Server:**
   - Configured to automatically assign IP addresses to DHCP clients within the defined networks.

#### Network Configuration:

- **Network 1 (192.168.1.0/24):**
  - **DHCP Server:** Configured with a pool of IP addresses ranging from 192.168.1.100 to 192.168.1.200.
  - **Router Interface:** Assigned IP address 192.168.1.1.
  - **PC1:** DHCP client configured to obtain IP address dynamically.

- **Network 2 (10.0.0.0/24):**
  - **DHCP Server:** Configured with a pool of IP addresses ranging from 10.0.0.100 to 10.0.0.200.
  - **Router Interface:** Assigned IP address 10.0.0.1.
  - **PC2:** DHCP client configured to obtain IP address dynamically.

#### DHCP Configuration:

- **DHCP Server Settings:**
  - **Network 1:**
    ```text
    subnet 192.168.1.0 netmask 255.255.255.0 {
        range 192.168.1.100 192.168.1.200;
        option routers 192.168.1.1;
        option domain-name-servers 8.8.8.8, 8.8.4.4;
        default-lease-time 600;
        max-lease-time 7200;
    }
    ```

  - **Network 2:**
    ```text
    subnet 10.0.0.0 netmask 255.255.255.0 {
        range 10.0.0.100 10.0.0.200;
        option routers 10.0.0.1;
        option domain-name-servers 8.8.8.8, 8.8.4.4;
        default-lease-time 600;
        max-lease-time 7200;
    }
    ```

#### Simulation Steps:

1. **Configure Devices:**
   - Place routers, switches, and PCs on Packet Tracer workspace.
   - Assign IP addresses to router interfaces and PC network settings.

2. **DHCP Server Configuration:**
   - Configure DHCP pools on the DHCP server for each network.
   - Define IP address ranges, default gateway, DNS server addresses, lease durations, etc.

3. **Client Configuration:**
   - Set PCs as DHCP clients in their respective networks.
   - PCs should be configured to obtain IP addresses automatically.

4. **Testing:**
   - Power on PCs and observe DHCP process:
     - PCs send DHCP Discover messages.
     - DHCP server responds with DHCP Offer.
     - PCs send DHCP Request and DHCP server acknowledges with DHCP Acknowledge (DHCPACK).
     - Verify IP address assignment on PCs and connectivity between them across different networks.

### Conclusion:

Simulating DHCP on Packet Tracer demonstrates the functionality of automatic IP address assignment within multiple network environments. This setup showcases the practical implementation of DHCP for network administration and management.

