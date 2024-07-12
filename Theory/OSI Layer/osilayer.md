# Computer Networks Assignment

## Question 1: What layer controls the wires?

### Answer

In the OSI (Open Systems Interconnection) model, the **Physical Layer** is responsible for controlling the wires and the physical medium through which data is transmitted. This layer is the first and lowest layer in the OSI model.

The Physical Layer deals with the following aspects:

- **Transmission Media:** The actual physical connection between devices. This includes cables (such as twisted pair, coaxial, and fiber optic) and wireless transmission.
- **Signal Transmission:** Converting data into electrical, optical, or radio signals suitable for transmission over the chosen medium.
- **Data Rate Control:** Defining the rate at which data is transmitted over the physical medium, often measured in bits per second (bps).
- **Bit Representation:** Determining how bits are represented on the physical medium, including encoding and modulation techniques.
- **Physical Topology:** Defining the physical layout of the network, such as bus, ring, star, and mesh topologies.
- **Synchronization:** Ensuring that the sender and receiver are synchronized at the bit level, often using clock signals.

In summary, the Physical Layer is crucial for establishing, maintaining, and deactivating the physical connection between network devices, making it responsible for controlling the wires and other physical aspects of the network infrastructure.

---

## Question 2: How can you tell one device apart from another at this layer?

### Answer

At the **Physical Layer** of the OSI model, devices are distinguished from one another using **hardware addresses** or **physical addresses**. These addresses are unique identifiers assigned to network interfaces at the hardware level.

### Key Methods of Differentiation:

- **MAC Address:** The most common method for distinguishing devices at the physical layer is the **MAC (Media Access Control) address**. Each network interface card (NIC) has a unique MAC address, which is a 48-bit identifier typically represented as a sequence of 12 hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E).
  - **Unicast Address:** Used for identifying a single unique network interface.
  - **Broadcast Address:** Used for sending data to all devices on the network.
  - **Multicast Address:** Used for sending data to a group of devices.

### How MAC Addresses Work:

- **Permanent Assignment:** MAC addresses are usually assigned by the manufacturer of the NIC and are intended to be unique to each device.
- **Address Resolution:** Network devices use the Address Resolution Protocol (ARP) to map network layer addresses (such as IP addresses) to MAC addresses.
- **Frame Identification:** In Ethernet networks, each frame (data packet) includes both the source and destination MAC addresses in its header, allowing devices to identify where the frame came from and where it should be sent.

### Practical Example:

When a data packet arrives at a switch, the switch uses the destination MAC address in the packet header to determine which port to forward the packet to, ensuring it reaches the correct device. This mechanism helps differentiate between multiple devices connected to the same network.

---

### OSI Model Layers

For context, here is a brief overview of the seven layers of the OSI model:

1. **Physical Layer:** Controls the physical connection between devices.
2. **Data Link Layer:** Handles error detection, correction, and frames.
3. **Network Layer:** Manages logical addressing and routing.
4. **Transport Layer:** Ensures end-to-end communication, error recovery, and flow control.
5. **Session Layer:** Manages sessions between applications.
6. **Presentation Layer:** Translates data between the application layer and the network.
7. **Application Layer:** Provides network services to end-user applications.

Understanding the role of each layer helps in grasping the comprehensive functionality of the OSI model in computer networks.

---

### Additional Resources

- [OSI Model Explained](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [Physical Layer in Computer Network](https://www.geeksforgeeks.org/physical-layer-in-osi-model/)
- [MAC Addresses](https://www.lifewire.com/definition-of-mac-address-817508)

