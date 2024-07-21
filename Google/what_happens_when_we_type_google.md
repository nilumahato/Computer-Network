
# What Happens When We Type `google.com` and Press Enter in the Browser?

![GoogleFlow](https://github.com/user-attachments/assets/650892db-407c-47c6-a200-7174840bfa01)

## Detailed Explanation of Each Step

### Client Side (Client IP: 192.168.1.65)

#### 1. URL Parsing and Validation
- The browser parses the URL `google.com` to ensure it is valid and identifies the domain name to be accessed.

#### 2. Browser Cache for DNS Record
- Checks if `google.com` is already cached in the browser. If found, it skips further DNS lookups.

#### 3. OS Cache for DNS Record
- If not found in the browser cache, the browser checks the operating system's DNS cache.

### Router/Gateway (Router Public IP: 27.34.108.XX)

#### 4. Router Cache for DNS Record
- The router checks its own DNS cache for the domain name.

#### 5. NAT Table Entry Creation
- The router creates an entry in the NAT (Network Address Translation) table, mapping the client’s private IP and port (`192.168.1.65:12345`) to a public IP and port (`27.34.108.XX:46789`). The DNS server IP and port are `8.8.8.8:53`.

#### 6. DNS Recursive Resolver Query
- If the record is not found in the router cache, the router forwards the DNS query to the ISP's DNS server.

##### 6.1 DNS Root Name Server Query
- The ISP's DNS server may query a DNS Root Name Server if it does not have the answer.

##### 6.2 DNS TLD Name Server Query
- The query goes to the TLD (Top-Level Domain) name server for `.com`.

##### 6.3 Google Authoritative Name Server Query
- The query is forwarded to Google's authoritative name server for `google.com`.

#### 7. DNS Resolution
- The authoritative name server resolves `google.com` to its IP address (`142.250.207.238`).

#### 8. DNS Response
- The DNS server sends the resolved IP address back to the router.

### Client Side (Client IP: 192.168.1.65)

#### 9. Initialize TCP Connection
- The client starts a TCP connection to the IP address `142.250.207.238`.

### Router/Gateway (Router Public IP: 27.34.108.XX)

#### 10. NAT Table Update
- The router updates the NAT table with the private IP (`192.168.1.65`), private port (`45678`), public IP (`27.34.108.XX`), and public port (`56789`). The destination IP and port are `142.250.207.238:443`.

### TCP Connection and TLS Handshake (Client, Router, Server)

#### 11. TCP Handshake - SYN Packet
- The client sends a SYN (synchronize) packet to the server.

#### 12. TCP Handshake - SYN-ACK Packet
- The server responds with a SYN-ACK (synchronize-acknowledge) packet.

#### 13. TCP Handshake - ACK Packet
- The client sends an ACK (acknowledge) packet, completing the three-way handshake.

#### 14. TCP Connection Established
- The TCP connection is established between the client and server.

#### 15. TLS Handshake Initiation
- The client initiates a TLS (Transport Layer Security) handshake to secure the communication.

#### 16. Client Hello
- The client sends a Client Hello message, which includes supported cipher suites and a client random value.

### Google Server Side (Google Server Public IP: 142.250.207.238)

#### 17. Server Hello
- The server responds with a Server Hello message, server random value, and its digital certificate.

#### 18. Certificate Validation
- The client validates the server's certificate against its list of trusted Certificate Authorities (CAs).

#### 19. Certificate Validation Success
- If the certificate is valid, the TLS handshake proceeds.

#### 20. Key Exchange and Change Cipher Spec
- The client sends a Client Key Exchange message, followed by Change Cipher Spec and Finished messages.

#### 21. Change Cipher Spec and Finished
- The server responds with its Change Cipher Spec and Finished messages.

### Encrypted HTTP Request and Response

#### 22. TLS Success - Encrypted Channel Established
- A secure TLS channel is established.
- **Symmetric Key Storage (Client RAM)**: Both client and server generate the same symmetric key used for encryption and decryption of the data transmitted over this secure channel.

#### 23. Encrypted HTTP Request
- The client sends an encrypted HTTP request to the server.

### Google Server Side (Google Server Public IP: 142.250.207.238)

#### 24. Encrypted Request Processing
- **Symmetric Key Storage (Server RAM)**: The server uses the symmetric key stored in its RAM to decrypt the incoming HTTP request.
- The server processes the decrypted request.

#### 25. Encrypted HTTP Response
- The server sends an encrypted HTTP response back to the client.

### Client Side (Client IP: 192.168.1.65)

#### 26. Decrypt HTTP Response
- The client decrypts the HTTP response using the symmetric key stored in its RAM.

#### 27. Generate Markup with Style and Interactivity
- The client processes the decrypted response, which typically contains HTML, CSS, and JavaScript, to generate markup with style and interactivity.

#### 28. Render Page
- The browser renders the webpage, displaying the content to the user.

### Additional Details:

#### Network Address Translation (NAT)
- **Private IP (Client)**: `192.168.1.65`
- **Public IP (Router)**: `27.34.108.XX`

NAT (Network Address Translation) maps the client's private IP address to the router's public IP address, allowing multiple devices on the local network to access the internet using a single public IP address.

**NAT Translation Example**:
- **Private IP:Private Port**: `192.168.1.65:45678`
- **Public IP:Public Port**: `27.34.108.XX:56789`
- **Destination IP:Destination Port**: `142.250.207.238:443`

By following these steps, the browser successfully retrieves and renders the `google.com` webpage, ensuring a secure and efficient browsing experience.
