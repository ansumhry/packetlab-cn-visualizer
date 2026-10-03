# Reflection — Computer Networks Dual-Layer Visualizer

## AI platform and model

I used ChatGPT with GPT-5.6 Luna to help me understand the project setup, review the documentation, and prepare the assignment submission. The guidance helped me work through the setup and testing steps. I reviewed the project by running the dashboard and checking its main interactions.

## Synchronization and design

PacketLab has two main panels. The left panel lets the user choose Browsing, Mail, or Streaming. The right panel displays the corresponding application-layer or transport-layer protocol events.

After selecting an activity, the simulator generates a related trace. The Application Layer and Transport Layer tabs show different views of the same activity. The Previous, Next, Pause/Resume, and Replay controls help the user examine the events step by step.

## Corrections and validation

I tested the application on my Windows PC using a desktop browser. I confirmed that the dashboard opened, the Visit page button generated a trace, and the Next button advanced through the protocol events.

These checks confirmed that the main demonstration flow worked during my testing. I did not record a specific code bug fix during these checks. The displayed protocol exchanges are simulations, so they should not be treated as real network packet captures.

## Protocol observations

* **Browsing:** DNS resolution is shown before the HTTP request and response. TCP establishes a connection before carrying the HTTP data and then closes the connection in the simplified example.
* **Mail:** SMTP uses commands and responses to represent a mail conversation over TCP. TCP transports a continuous byte stream, so SMTP commands do not necessarily correspond one-to-one with TCP segments.
* **Streaming:** The client requests a playlist and media segments. The simulator illustrates how media data can be delivered over a transport connection. Real streaming implementations may use different protocols and configurations.

## Limitations and next steps

PacketLab is an educational simulator, not a live packet-capture tool. The addresses, sequence numbers, payload sizes, and protocol messages are illustrative. It does not send real emails or stream actual video.

UDP and QUIC are not implemented in this version. Future improvements could include live packet-capture integration, UDP and QUIC comparisons, TLS state visualization, and more detailed TCP sequence-number and acknowledgement validation.

## Conclusion

Building and testing this dashboard helped me connect familiar activities, such as browsing a website, sending an email, and streaming media, with the protocols operating underneath them. The dual-panel design makes it easier to explore application-layer messages alongside transport-layer events.
