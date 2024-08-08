# Designing a System for Automatic IP Address Assignment

## Question:

Design a system for assigning IP addresses automatically to hosts on a network.

## Answer:

### DHCP System Design

#### Components:

1. **DHCP Server:**
   - Responsible for dynamically assigning IP addresses to DHCP clients on the network.
   - Manages a pool of available IP addresses and leases them to clients for a specific period.

2. **DHCP Client:**
   - Devices (computers, smartphones, printers, etc.) that request and obtain IP addresses from the DHCP server.

3. **DHCP Relay Agent (Optional):**
   - Facilitates communication between DHCP clients and servers when they are not on the same subnet.

#### Workflow:

1. **DHCP Discover:**
   - When a new device connects to the network, it broadcasts a DHCP Discover message to discover DHCP servers on the network.

2. **DHCP Offer:**
   - DHCP servers respond with a DHCP Offer message containing an available IP address, subnet mask, lease duration, and other configuration parameters.

3. **DHCP Request:**
   - The client selects one of the offered IP addresses and sends a DHCP Request message to the chosen DHCP server.

4. **DHCP Acknowledge (DHCPACK):**
   - The DHCP server confirms the IP address assignment by sending a DHCP Acknowledge message to the client.

5. **Lease Management:**
   - The DHCP server maintains a lease database, tracking which IP addresses are assigned to which clients and for how long.

6. **Renewal and Release:**
   - Clients periodically renew their lease by requesting to extend the IP address lease duration.
   - Clients can release their IP address when disconnecting from the network.

#### Implementation Details:

- **IP Address Pool:** Defines a range of IP addresses that the DHCP server can assign to clients.
- **Lease Duration:** Specifies how long IP addresses are leased to clients before they must be renewed.
- **Configuration Parameters:** Includes options such as subnet mask, default gateway (routers), DNS server addresses, default lease time, and maximum lease time.
- **Security:** Implement measures like DHCP snooping to prevent unauthorized DHCP servers from operating on the network.

#### Example Configuration:

```text
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option domain-name-servers 8.8.8.8, 8.8.4.4;
    default-lease-time 600;
    max-lease-time 7200;
}
