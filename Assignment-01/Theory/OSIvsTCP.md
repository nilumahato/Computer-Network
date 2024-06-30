## What is TCP/IP Model?

The Internet protocol suite, commonly known as TCP/IP, is a framework for organizing the set of communication protocols used in the Internet and similar computer networks according to functional criteria. The foundational protocols in the suite are the Transmission Control Protocol (TCP), the User Datagram Protocol (UDP), and the Internet Protocol (IP)

![TCP/IP Model](https://cheapsslsecurity.com/blog/wp-content/uploads/2022/06/tcp-ip-model-layers-and-their-functions.png)

## Differences Between OSI Model and TCP/IP Model

| Feature             | OSI Model                                   | TCP/IP Model                                 |
|---------------------|---------------------------------------------|----------------------------------------------|
| **Full Form**       | Open Systems Interconnection Model         | Transmission Control Protocol/Internet Protocol Model |
| **Developed By**    | International Organization for Standardization (ISO) | Department of Defense (DoD)                  |
| **Number of Layers**| 7                                           | 4                                            |
| **Layers**          | 1. Physical                                 | 1. Network Interface                         |
|                     | 2. Data Link                                | 2. Internet                                  |
|                     | 3. Network                                  | 3. Transport                                 |
|                     | 4. Transport                                | 4. Application                               |
|                     | 5. Session                                  |                                              |
|                     | 6. Presentation                             |                                              |
|                     | 7. Application                              |                                              |
| **Layer Interaction**| Each layer serves the layer above and is served by the layer below | Layers are more closely integrated with fewer distinct boundaries |
| **Protocol Dependency**| Protocols are better defined and not dependent on any specific protocols | Protocols are designed around the TCP/IP suite |
| **Flexibility**     | More flexible in terms of fitting different protocols at each layer | More rigid as it is tightly linked to the suite of TCP/IP protocols |
| **Usage**           | Primarily used as a reference model for understanding and designing networks | Widely used in practice for real-world networking |
| **Standardization** | Provides a conceptual framework for standardization of various network protocols | Focused on a suite of protocols that are already standardized and widely adopted |
| **Addressing**      | Uses different addressing schemes for different layers | Primarily uses IP addresses for identifying devices on the network |
| **Error Handling**  | Error handling is done at multiple layers including the Data Link and Transport layers | Primarily handled at the Transport layer through TCP |

## Summary

- **OSI Model**: A theoretical framework used to understand and design networks. It has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.
- **TCP/IP Model**: A practical framework for real-world networking. It has 4 layers: Network Interface, Internet, Transport, and Application.
