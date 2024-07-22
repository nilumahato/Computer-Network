# What Happens When You Type `google.com` and Press Enter

![GoogleFlow](https://github.com/user-attachments/assets/650892db-407c-47c6-a200-7174840bfa01)

This document explains the detailed steps that occur from the moment you type `google.com` into your browser and press enter until the webpage is displayed. It covers network, DNS, TCP/IP, and HTTP/HTTPS concepts.

## 1. URL Parsing and Validation
- **URL Parsing**: When you type `google.com` in the browser, the browser parses the URL to identify the domain name. This process involves breaking down the URL into its components, such as the protocol (HTTP or HTTPS), host (google.com), path, query parameters, etc.
- **Validation**: The browser checks if the URL is correctly formatted and whether it's a valid URL. If the URL is invalid, the browser displays an error message.

## 2. Browser Cache for DNS Record
- **Browser Cache**: The browser checks its local cache to see if it has a recent DNS record for `google.com`. DNS records include the IP address of the server associated with the domain. If found, it uses this cached record to avoid repeating the DNS lookup process.

## 3. OS Cache for DNS Record
- **Operating System Cache**: If the browser cache doesn’t contain the DNS record, the browser requests the DNS record from the operating system. The OS maintains a DNS cache to speed up the resolution process for recently accessed domains.

## 4. Router Cache for DNS Record
- **Router Cache**: If neither the browser nor the OS has the cached DNS record, the request is forwarded to the router. The router maintains its own DNS cache and may already have the necessary DNS record.

## 5. NAT Table Entry Creation
- **Network Address Translation (NAT)**: The router creates an entry in its NAT table, mapping the client’s internal private IP address and port (e.g., `192.168.1.65:12345`) to a public IP address and port (e.g., `27.34.108.XX:46789`). NAT allows multiple devices on a local network to share a single public IP address for internet access.

## 6. DNS Recursive Resolver Query
- **DNS Recursive Resolver**: If the router’s cache doesn’t have the record, it forwards the DNS query to the ISP’s DNS server. This server attempts to resolve the domain name by querying other DNS servers.

### 6.1 DNS Root Name Server Query
- **Root Name Server**: If the ISP’s DNS server can’t resolve the name, it queries a root DNS server. Root servers know the addresses of TLD (Top-Level Domain) servers (e.g., `.com`, `.org`).

### 6.2 DNS TLD Name Server Query
- **TLD Name Server**: The root server directs the query to the appropriate TLD name server, responsible for the `.com` domain.

### 6.3 Google Authoritative Name Server Query
- **Authoritative Name Server**: The TLD server directs the query to Google’s authoritative name server, which has the final DNS record for `google.com`.

## 7. DNS Resolution
- **Resolved Hostname to IP**: The authoritative name server returns the IP address for `google.com` (e.g., `142.250.207.238`). This IP address is sent back through the DNS hierarchy to the ISP’s DNS server.

## 8. DNS Response
- **DNS Response**: The ISP’s DNS server sends the resolved IP address back to the router, which forwards it to the client’s operating system and ultimately to the browser.

## 9. Initialize TCP Connection
- **TCP Connection Initiation**: With the IP address obtained, the client’s browser initiates a TCP connection to `142.250.207.238`. TCP (Transmission Control Protocol) ensures reliable, ordered, and error-checked delivery of data.

## 10. NAT Table Update
- **NAT Update**: The router updates its NAT table to reflect the mapping from the client’s private IP and port to the public IP and port and the destination IP and port.

## 11-13. TCP Handshake (Client, Router, Server)
- **11. SYN Packet**: The client sends a SYN (synchronize) packet to the server to start the TCP handshake. This packet includes a sequence number.
- **12. SYN-ACK Packet**: The server responds with a SYN-ACK (synchronize-acknowledge) packet, acknowledging the client’s sequence number and sending its own.
- **13. ACK Packet**: The client responds with an ACK (acknowledge) packet, acknowledging the server’s sequence number. This completes the three-way handshake, establishing a TCP connection.

## 14. TCP Connection Established
- **TCP Connection**: The connection is now established, allowing data to be transmitted between the client and server reliably.

## 15. TLS Handshake Initiation
- **TLS Handshake**: To secure the communication, the client initiates a TLS handshake. TLS (Transport Layer Security) ensures that the data exchanged is encrypted and secure.

## 16. Client Hello
- **Client Hello**: The client sends a "Client Hello" message to the server, which includes information about supported cipher suites, TLS version, and a randomly generated value.

## 17. Server Hello
- **Server Hello**: The server responds with a "Server Hello" message, including its chosen cipher suite, TLS version, a randomly generated value, and its digital certificate.

## 18. Certificate Validation
- **Certificate Validation**: The client validates the server’s digital certificate against its list of trusted Certificate Authorities (CAs). This step ensures that the server is legitimate and not an imposter.

## 19. Certificate Validation Success
- **Validation Success**: If the certificate is valid, the handshake continues. If not, the client aborts the connection.

## 20-21. Key Exchange and Change Cipher Spec
- **20. Key Exchange**: The client and server exchange keys using the previously agreed-upon method (e.g., Diffie-Hellman). The client then sends a "Change Cipher Spec" message to switch to encrypted communication, followed by a "Finished" message.
- **21. Change Cipher Spec and Finished**: The server responds with its own "Change Cipher Spec" and "Finished" messages, completing the TLS handshake.

## 22. TLS Success - Encrypted Channel Established
- **Encrypted Channel**: A secure, encrypted channel is now established between the client and server, using symmetric encryption for data transmission.

## 23. Encrypted HTTP Request
- **Encrypted Request**: The client sends an encrypted HTTP request over the secure channel. This request might be an HTTP GET request for the homepage of `google.com`.

## 24-25. Encrypted HTTP Response
- **24. Encrypted Response**: The server processes the request and sends back an encrypted HTTP response, containing the requested webpage data.
- **25. Decrypt HTTP Response**: The client decrypts the HTTP response using the symmetric key established during the TLS handshake.

## 26-28. Rendering the Webpage
- **26. Generate Markup**: The client’s browser generates markup from the response, which includes HTML, CSS, and JavaScript.
- **27. Render Page**: The browser processes the markup and renders the webpage, displaying the content to the user.
- **28. Additional Resources**: The browser may need to make additional requests to load other resources like images, scripts, and stylesheets, repeating the DNS, TCP, and TLS steps as necessary.

## Additional Details: NAT and DNS
- **NAT (Network Address Translation)**: NAT translates private IP addresses to a public IP address, allowing multiple devices on a local network to share a single public IP. This is crucial for conserving public IP addresses and providing security by hiding internal network structure.
- **DNS (Domain Name System)**: DNS translates human-readable domain names (e.g., google.com) into IP addresses that computers use to identify each other on the network. It involves a hierarchical structure with root servers, TLD servers, and authoritative servers to resolve domain names efficiently.

By following these steps, the browser successfully retrieves and displays the `google.com` webpage, ensuring a secure and efficient user experience.
