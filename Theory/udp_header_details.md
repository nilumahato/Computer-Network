## Question
How many bytes is the UDP header? What are the different fields? How are the values set?

## Answer

### UDP Header Size

The User Datagram Protocol (UDP) header is **8 bytes** (or 64 bits) in size.

### Fields in the UDP Header

The UDP header consists of four fields:

| Field               | Size (bits) | Description                                                                                 |
|---------------------|-------------|---------------------------------------------------------------------------------------------|
| Source Port         | 16          | The port number of the application at the sender's side.                                  |
| Destination Port    | 16          | The port number of the application at the receiver's side.                                 |
| Length              | 16          | The total length of the UDP header and the data.                                          |
| Checksum            | 16          | Used for error-checking the header and data.                                              |

### How Field Values are Set

1. **Source Port**: Set by the application that is creating the UDP datagram. It should correspond to the local port number that the application is listening on.

   Example: If a DNS server sends a response from port 53, the Source Port will be set to 53.

2. **Destination Port**: Set by the application sending the datagram, indicating the target port on the receiving device.

   Example: If the destination is a web server listening on port 80, the Destination Port will be set to 80.

3. **Length**: Calculated by the sender by adding 8 bytes (the size of the header) to the size of the data being sent.

   Example: If the payload data is 32 bytes, the Length will be set to 40 (8 + 32).

4. **Checksum**: Calculated by the sender using a specific algorithm that involves summing the UDP header and data, followed by computing the 1's complement.

   Example: If the checksum calculation results in 0x1A2B, this value will be set in the Checksum field.

### Example of a UDP Header

Below is an illustration of a UDP header with field sizes:

![UDP Header](https://notes.shichao.io/tcpv1/figure_10-2.png)

### Conclusion

The UDP header is a simple, fixed-size structure that facilitates fast and efficient data transmission without the overhead of connection management. Each field has a specific purpose in ensuring that data is sent correctly.
