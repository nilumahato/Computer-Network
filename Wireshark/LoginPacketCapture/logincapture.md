# Login Traffic Analysis

Here we have analyzed network traffic using Wireshark and Burp Suite. This analysis focuses on the raw request and response, VERB/ METHOD used, protocol, version and security mechanism used during the transmission.

## Tools Used

- **Wireshark**: A network protocol analyzer used to capture and analyze network traffic.
- **Burp Suite**: A web vulnerability scanner used to intercept and inspect HTTP requests and responses.

## Analysis

### Burp Suite

Burp Suite was used to intercept and inspect the login request to the server.


!(Login Page Traffic)[../../Images/LoginPageLoad.png]
From above figure, we can observe the following: 

#### Request Analysis
The first line of a HTTP request is known as request line. 

- __Protocol__: HTTP
- __Version__: 1.1
- __Method__: GET
- __Endpoint__:/Login

Below this are the HTTP headers and there will be the request body at the last which is generally not found in the GET request method.

#### Response Analysis 
The first line of a HTTP response is known as response line.
- __Protocol__: HTTP
- __Version__: 1.1
- __StatusCode__:200 
- __Reason Phrase__:OK

The fields between response body and respone line are response headers which really defines different characteristics about the response.

!(Login Traffic)[../../Images/LoginToWebsite.png]

#### Request Analysis
- __Protocol__: HTTP
- __Version__: 1.1
- __Method__: POST
- __Endpoint__:/Login

Below this are the HTTP headers and there is the request body at the last which containes username and password field and is in a JSON format. 

#### Response Analysis 
- __Protocol__: HTTP
- __Version__: 1.1
- __StatusCode__:200 
- __Reason Phrase__:OK

The fields between response body and respone line are response headers which really defines different characteristics about the response. We can see the json response and also the Set-Cookie headers with some value which will be set in the browser, and can be used for authentication and other purposes.

### Wireshark

Using wireshark we can see the communication was between the client (192.168.1.65) and the server (202.70.67.149). We can see:
- Multiple HTTP GET and POST requests.
- Responses indicating successful authentication.
- HTTP/1.1 protocol with JSON payloads.
!(Different Layers of Packet)[../../Images/DifferentLayers.png]

`Note: We can see that non of the traffic were encrypted using any encryption such as SSL/TLS. If it was used we wouldnot be able to inspect the traffic in its raw format from the wireshark.`

### Follow HTTP Stream

Using Wireshark's "Follow HTTP Stream" feature, the detailed HTTP communication between the client and server was analyzed. This includes:
- Request headers and body.
- Response headers and body.
- Cookies and other metadata.
!(Following HTTP Stream)[../../Images/FollowHTTPStream.png]

## Conclusion

This analysis demonstrates the use of Wireshark and Burp Suite to capture/intercept, inspect, and analyze HTTP traffic. 

