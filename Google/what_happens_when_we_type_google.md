# What Happens When We Type `google.com` and Press Enter in the Browser?
![GoogleFlow](https://github.com/user-attachments/assets/650892db-407c-47c6-a200-7174840bfa01)

## 1. URL Parsing and Validation
- The browser parses the URL to check if it is valid and determines the domain name to access.

## 2. Browser Cache for DNS Record
- The browser checks its cache for a DNS (Domain Name System) record of `google.com`.

## 3. OS Cache for DNS Record
- If the DNS record is not found in the browser cache, the operating system cache is checked using operating system services.

## 4. DNS Query Process to Router
- If the DNS record is not found in the OS cache, the client sends a DNS query to the router (Router/Gateway).

## 5. Router Cache for DNS Record
- The router checks its cache for the DNS record.

## 6. DNS Recursive Resolver Query
- If the DNS record is not found in the router cache, the router forwards the DNS query to the configured DNS server (typically the ISP's DNS server).

## 6.1 DNS Root Name Server Query
- The query is forwarded to the DNS Root Name Server.

## 6.2 DNS TLD Name Server Query
- The query is forwarded to the TLD (Top-Level Domain) Name Server for `.com` domains.

## 6.3 Google Authoritative Name Server Query
- The query is forwarded to the Google Authoritative Name Server.

## 7. DNS Resolution
- The authoritative name server responds with the IP address for `google.com`.

## 8. DNS Response to Router
- The DNS response is sent back to the router.

## 9. Router Cache Update
- The router caches the DNS response.

## 10. DNS Response to Client
- The router sends the DNS response back to the client.

## 11. TCP Handshake Initiation
- The client initiates a TCP (Transmission Control Protocol) connection to the resolved IP address of `google.com`.

## 12. SYN Packet
- The client sends a SYN (synchronize) packet to the server.

## 13. SYN-ACK Packet
- The server responds with a SYN-ACK (synchronize-acknowledge) packet.

## 14. ACK Packet
- The client sends an ACK (acknowledge) packet, establishing the TCP connection.

## 15. TLS Handshake Initiation
- The client initiates a TLS (Transport Layer Security) handshake to secure the connection.

## 16. Client Hello
- The client sends a Client Hello message, including a list of supported cipher suites and a random number.

## 17. Server Hello
- The server responds with a Server Hello message, selecting a cipher suite and sending its certificate along with a random number.

## 18. Certificate Validation
- The client validates the server's certificate against a list of trusted Certificate Authorities (CAs).

## 19. Certificate Validation Success
- If the certificate is valid, the client proceeds with the TLS handshake.

## 20. Key Exchange and Change Cipher Spec
- The client and server exchange keys and the client sends a Change Cipher Spec message, indicating that future messages will be encrypted.

## 21. Finished Message
- The client and server send Finished messages to each other, completing the TLS handshake.

## 22. Encrypted HTTP Request
- The client sends an encrypted HTTP request to the server.

## 23. Encrypted HTTP Response
- The server encrypts the HTTP response and sends it back to the client.

## 24. Decrypt HTTP Response
- The client decrypts the HTTP response using the symmetric key established during the TLS handshake.

## 25. Process Decrypted Response
- The client processes the decrypted HTTP response.

## 26. Render Web Page
- The browser generates markup with style and interactivity and renders the webpage to the user.

## Detailed Flow with Diagram Annotations

### Client Side (Client IP: 192.168.1.65)
1. **URL Parsing and Validation**
    - Browser parses the URL and checks if it's valid.

2. **Browser Cache for DNS Record**
    - Checks if `google.com` is in the browser cache.

3. **OS Cache for DNS Record**
    - Uses operating system services to check OS cache.

4. **DNS Query to Router**
    - Sends DNS query to router if not found in caches.

### Router/Gateway (Router Public IP: 27.34.108.XX)
5. **Router Cache for DNS Record**
    - Router checks its cache for the DNS record.

6. **DNS Recursive Resolver Query**
    - Forwards DNS query to ISP's DNS server if not found.

6.1 **DNS Root Name Server Query**
    - Query goes to DNS Root Name Server.

6.2 **DNS TLD Name Server Query**
    - Query goes to TLD Name Server for `.com`.

6.3 **Google Authoritative Name Server Query**
    - Query goes to Google's authoritative name server.

7. **DNS Resolution**
    - Google server responds with IP address `142.250.207.238`.

8. **DNS Response to Router**
    - Response sent back to the router.

9. **Router Cache Update**
    - Router caches the DNS response.

10. **DNS Response to Client**
    - Router sends DNS response to the client.

### TCP Connection and TLS Handshake (Client, Router, Server)
11. **TCP Handshake Initiation**
    - Client initiates TCP connection to IP `142.250.207.238`.

12. **SYN Packet**
    - Client sends SYN packet to the server.

13. **SYN-ACK Packet**
    - Server responds with SYN-ACK packet.

14. **ACK Packet**
    - Client sends ACK packet, establishing connection.

15. **TLS Handshake Initiation**
    - Client starts TLS handshake for secure connection.

16. **Client Hello**
    - Client sends Client Hello with cipher suites.

17. **Server Hello**
    - Server responds with Server Hello and certificate.

18. **Certificate Validation**
    - Client validates server certificate.

19. **Certificate Validation Success**
    - If valid, TLS handshake proceeds.

20. **Key Exchange and Change Cipher Spec**
    - Keys are exchanged, and encryption is established.

21. **Finished Message**
    - Client and server send Finished messages.

### HTTP Request and Response (Client, Router, Server)
22. **Encrypted HTTP Request**
    - Client sends encrypted HTTP request.

23. **Encrypted HTTP Response**
    - Server sends encrypted HTTP response.

24. **Decrypt HTTP Response**
    - Client decrypts HTTP response using symmetric key.

25. **Process Decrypted Response**
    - Client processes decrypted response.

26. **Render Web Page**
    - Browser renders the webpage to the user.

This step-by-step explanation corresponds to the numbers in the image and provides a detailed overview of the process when you type `google.com` and press enter in the browser.
