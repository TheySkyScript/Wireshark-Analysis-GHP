Wireshark Network Traffic Analysis Report
Introduction

This project focused on analyzing real network traffic captured in a packet capture (.pcap) file using Python and the PyShark library. The purpose of the analysis was to better understand network behavior by examining packet frequency, bandwidth usage, protocol distribution, packet sizes, and the most active source IP addresses. The project demonstrates how packet capture data can be transformed into meaningful visualizations and insights for cybersecurity, troubleshooting, and performance monitoring.

Tools and Technologies Used

The analysis was completed using Python with several libraries:

PyShark for reading and processing the .pcap file
Pandas for storing and organizing the packet data
Matplotlib and Seaborn for data visualization
Wireshark packet capture data as the source of network traffic information

The script extracted the following fields from each packet:

Timestamp
Packet length
Highest protocol layer
Source IP address
Destination IP address

These fields were then used to create multiple graphs and summaries of the network activity.

Packet Traffic Over Time

The “Packets per Second” graph shows that network activity fluctuated significantly during the capture period. Most seconds contained between 10 and 60 packets, but there were several spikes where traffic exceeded 100 packets per second. The highest spike occurred near the beginning of the capture, reaching approximately 145 packets in a single second.

These spikes likely represent bursts of user activity such as opening websites, streaming content, loading applications, or transferring data. The graph also shows that traffic levels returned to lower values after these spikes, suggesting that the traffic was burst-based rather than constant.

Bandwidth Usage Over Time

The “Bytes per Second” graph reveals a similar pattern to the packets-per-second graph, but it provides more detail about the amount of data being transferred. The highest peak reached around 150,000 bytes in a second, which indicates a brief but large transfer of data.

After the initial spike, most traffic remained below 20,000 bytes per second, with occasional peaks around 30,000 to 50,000 bytes. This suggests that the network was not continuously transferring large files but instead experienced periodic bursts of activity.

The relationship between packets per second and bytes per second also suggests that some bursts involved larger packets, while others involved many smaller packets.

Protocol Distribution

The “Top Protocols” graph shows that the most common protocol category was DATA, followed by TCP and TLS. DATA packets made up the largest portion of the traffic, with nearly 800 packets observed. TCP and TLS both had over 400 packets each.

The high number of TCP packets indicates that the network traffic relied heavily on standard connection-oriented communication. The strong presence of TLS packets suggests that much of the traffic was encrypted, which is expected for modern internet browsing and secure online services.

Other protocols observed included:

RTCP
STUN
DNS
SSDP
ARP
ICMPv6

The presence of DNS packets indicates normal hostname resolution activity, while ARP packets show local network address resolution. STUN and RTCP traffic may indicate voice, video, or real-time communication services such as video calls or streaming applications.

One unusual observation is the appearance of “_WS.MALFORMED” packets. These packets may indicate incomplete, corrupted, or improperly decoded packets during capture. While only a moderate number were present, they may warrant further investigation if this traffic came from a production network.

Packet Size Distribution

The packet size distribution graph shows that most packets were relatively small, especially in the range below 200 bytes. Small packets are common for acknowledgments, DNS queries, and control traffic.

There was also a second concentration of larger packets between approximately 1,100 and 1,300 bytes. These larger packets likely represent data-heavy traffic such as file transfers, website content, streaming, or encrypted application traffic.

The presence of both small and large packets suggests a mix of lightweight control traffic and larger content-delivery traffic occurring during the capture period.

Top Source IP Addresses

The source IP analysis showed that two IP addresses dominated the traffic:

192.168.0.161
74.125.250.241

The address 192.168.0.161 is a private local network address, which was likely the main device generating the traffic during the capture. The address 74.125.250.241 is a public IP address associated with external internet services, likely from a major provider such as Google.

Other active IP addresses included:

169.150.254.94
172.217.19.14
192.168.0.1
192.178.162.139

The local router address, 192.168.0.1, also appeared in the traffic, which is expected because it serves as the gateway between the local device and the internet.

Rolling Average Analysis

The rolling average packets-per-second graph helps smooth out short-term fluctuations and provides a better view of overall traffic trends. The rolling average remained mostly between 20 and 45 packets per second throughout the capture.

This shows that while there were sudden bursts of traffic, the average activity level on the network remained moderate and stable. There were no signs of sustained overload, denial-of-service behavior, or extremely abnormal traffic patterns.

Conclusion

Overall, the network traffic appeared normal and consisted mostly of standard encrypted web traffic, DNS lookups, and some real-time communication protocols. The traffic showed brief bursts of high activity but generally remained at a moderate level.

The results demonstrate how Python can be used to automate Wireshark-style traffic analysis and generate useful visualizations. This type of analysis can be applied in cybersecurity, network troubleshooting, performance monitoring, and incident response. It also highlights the importance of understanding packet sizes, protocol usage, and traffic sources when analyzing network behavior.
