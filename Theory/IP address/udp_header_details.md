# Computer Network Assignment

## Question
How many bytes is the UDP header? What are the different fields? How are the field values set?

## Answer

### UDP Header Size

The User Datagram Protocol (UDP) header is **8 bytes** (or 64 bits) in size.

### Fields in the UDP Header

The UDP header consists of four fields:

1. **Source Port (16 bits / 2 bytes)**
   - This field identifies the port of the application sending the datagram. If the source port is not needed, it may be set to zero.

2. **Destination Port (16 bits / 2 bytes)**
   - This field identifies the port of the application receiving the datagram. This value is set by the sender to indicate where the data should be directed.

3. **Length (16 bits / 2 bytes)**
   - This field indicates the total length of the UDP header and the data in bytes. It is calculated by adding the length of the header (8 bytes) to the length of the payload. 

4. **Checksum (16 bits / 2 bytes)**
   - This field is used for error-checking the header and data. It is optional in IPv4 but mandatory in IPv6. The checksum is computed by taking the 1's complement of the sum of all 16-bit words in the header and data.

### How Field Values are Set

- **Source Port**: Set by the application that is creating the UDP datagram. It should correspond to the local port number that the application is listening on.
  
- **Destination Port**: Set by the application sending the datagram, indicating the target port on the receiving device. 

- **Length**: Calculated by the sender by adding 8 bytes (the size of the header) to the size of the data being sent. This value is then included in the header.

- **Checksum**: Calculated by the sender using a specific algorithm that involves summing the UDP header and data, followed by computing the 1's complement. This value is set in the checksum field to help the receiver verify data integrity.

