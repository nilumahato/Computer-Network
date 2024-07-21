# What Happens When We Type `google.com` and Press Enter in the Browser?
![GoogleFlow](https://github.com/user-attachments/assets/650892db-407c-47c6-a200-7174840bfa01)

## Detailed Explanation of Each Step

### Client Side (Client IP: 192.168.1.65)

#### 1. URL Parsing and Validation
- The browser takes the URL entered (`google.com`) and parses it to ensure it is valid. It checks for the correct format and identifies the domain name to be accessed.

#### 2. Browser Cache for DNS Record
- The browser first checks its internal cache to see if it already has a DNS record for `google.com`. If the record is found, it can skip further DNS lookups, reducing latency.

#### 3. OS Cache for DNS Record
- If the DNS record is not found in the browser cache, the browser queries the operating system's DNS cache. The OS maintains a cache of DNS lookups to speed up the resolution process.

#### 4. DNS Query to Router
- If the DNS record is not found in the OS cache, the client sends a DNS query to the local router. The router acts as the gateway to the internet and handles requests from multiple devices on the network.

### Router/Gateway (Router Public IP: 27.34.108.XX)

#### 5. Router Cache for DNS Record
- The router checks its own DNS cache to see if it has a recent record for `google.com`. This local caching helps in reducing the need for repeated DNS queries to external servers.

#### 6. DNS Recursive Resolver Query
- If the DNS record is not found in the router cache, the router forwards the DNS query to the configured DNS server, typically provided by the ISP. This server will handle the DNS resolution process.

##### 6.1 DNS Root Name Server Query
- The DNS server may query a DNS Root Name Server if it does not have the answer. The root server knows where to find the authoritative servers for all top-level domains (TLDs).

##### 6.2 DNS TLD Name Server Query
- The query is then forwarded to the TLD name server for `.com` domains. The TLD server directs the query to the authoritative name server for `google.com`.

##### 6.3 Google Authoritative Name Server Query
- Finally, the query reaches Google's authoritative name server, which has the DNS record for `google.com`. It responds with the IP address associated with the domain.

#### 7. DNS Resolution
- The authoritative name server responds with the IP address for `google.com`, e.g., `142.250.207.238`.

#### 8. DNS Response to Router
- The DNS response, containing the IP address, is sent back to the router.

#### 9. Router Cache Update
- The router caches the DNS response to expedite future requests for the same domain.

#### 10. DNS Response to Client
- The router sends the DNS response to the client, providing the necessary IP address to establish a connection.

### TCP Connection and TLS Handshake (Client, Router, Server)

#### 11. TCP Handshake Initiation
- The client begins a TCP (Transmission Control Protocol) connection to the resolved IP address (`142.250.207.238`). TCP is used to ensure a reliable and ordered data transmission.

#### 12. SYN Packet
- The client sends a SYN (synchronize) packet to the server to initiate the connection. This is the first step of the TCP three-way handshake.

#### 13. SYN-ACK Packet
- The server responds with a SYN-ACK (synchronize-acknowledge) packet, acknowledging the client's request and indicating readiness to establish a connection.

#### 14. ACK Packet
- The client sends an ACK (acknowledge) packet back to the server, completing the three-way handshake and establishing a TCP connection.

#### 15. TLS Handshake Initiation
- With the TCP connection established, the client initiates a TLS (Transport Layer Security) handshake to secure the communication channel.

#### 16. Client Hello
- The client sends a Client Hello message, which includes a list of supported cryptographic algorithms (cipher suites) and a random number used in the encryption process.

#### 17. Server Hello
- The server responds with a Server Hello message, selecting a cipher suite from the client's list. The server also sends its digital certificate and a random number.

#### 18. Certificate Validation
- The client validates the server's certificate against a list of trusted Certificate Authorities (CAs) to ensure the server's identity.

#### 19. Certificate Validation Success
- If the certificate is valid, the TLS handshake proceeds.

#### 20. Key Exchange and Change Cipher Spec
- The client and server exchange keys, and the client sends a Change Cipher Spec message, indicating that all further communications will be encrypted.

#### 21. Finished Message
- Both client and server send Finished messages, confirming that the TLS handshake is complete and encryption is established.

### HTTP Request and Response (Client, Router, Server)

#### 22. Encrypted HTTP Request
- The client sends an encrypted HTTP request to the server, such as a GET request for the `google.com` homepage.

#### 23. Encrypted HTTP Response
- The server processes the request and sends back an encrypted HTTP response containing the webpage data.

#### 24. Decrypt HTTP Response
- The client decrypts the HTTP response using the symmetric key established during the TLS handshake, making the data readable.

#### 25. Process Decrypted Response
- The client processes the decrypted response, which contains the HTML, CSS, JavaScript, and other resources needed to render the webpage.

#### 26. Render Web Page
- The browser generates the webpage's markup with style and interactivity, rendering it to the user.

### Additional Details:

#### Network Address Translation (NAT)
- **Private IP (Client)**: `192.168.1.65`
- **Public IP (Router)**: `27.34.108.XX`

NAT (Network Address Translation) is used to map the private IP address of the client to the public IP address of the router. This allows multiple devices on a local network to share a single public IP address for accessing the internet.

**NAT Translation Example**:
- **Private IP:Private Port**: `192.168.1.65:12345`
- **Public IP:Public Port**: `27.34.108.XX:46789`
- **Destination IP:Destination Port**: `142.250.207.238:443`

By following these steps, the browser successfully retrieves and renders the `google.com` webpage, ensuring a secure and efficient browsing experience.
