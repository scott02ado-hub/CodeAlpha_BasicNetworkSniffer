# Basic Network Sniffer - Project Report

## 1. Project Information

**Project Name:** CodeAlpha Basic Network Sniffer

**Domain:** Cyber Security

**Internship:** CodeAlpha Cyber Security Internship

**Developer:** Scott


---

# 2. Introduction

Network monitoring is an essential part of cybersecurity. Understanding how data flows across a network helps security professionals identify abnormal activities and potential threats.

This project implements a basic network sniffer using Python and Scapy. The application captures live network packets, analyzes their structure, and displays useful information about network communications.


---

# 3. Objectives

The main objectives of this project are:

- Capture live network traffic packets.
- Understand packet structures and protocols.
- Identify source and destination addresses.
- Analyze TCP and UDP communications.
- Implement packet logging.
- Develop practical knowledge of network security concepts.


---

# 4. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming language |
| Scapy | Packet capture and analysis |
| Rich | Terminal visualization |
| Git | Version control |
| Kali Linux | Testing environment |


---

# 5. Project Architecture

The project follows a modular architecture:
CodeAlpha_BasicNetworkSniffer

main.py
|
|
NetworkSniffer
|
+-- PacketAnalyzer
|
+-- PacketDisplay
|
+-- Logger




## Components

### Network Sniffer

Responsible for:

- Capturing packets from the network interface.
- Processing incoming traffic.
- Managing the capture lifecycle.


### Packet Analyzer

Responsible for extracting:

- Protocol type.
- Source IP.
- Destination IP.
- Source port.
- Destination port.
- Packet size.


### Display Module

Provides a professional terminal interface using Rich.


### Logger Module

Stores captured information for later analysis.


---

# 6. Installation

Install project dependencies:
pip install -r requirements.txt



---

# 7. Execution

The application requires administrator privileges for packet capture:
sudo .venv/bin/python main.py



Example interface:
CODEALPHA NETWORK SNIFFER

Captured Packet

Protocol TCP
Source 104.18.39.21:443
Destination 10.1.5.82:32818
Size 66 bytes



---

# 8. Testing Results

The application was successfully tested on Kali Linux.

Test results:

| Test | Result |
|------|--------|
| Application startup | PASS |
| Packet capture | PASS |
| TCP analysis | PASS |
| UDP analysis | PASS |
| Logging system | PASS |
| Terminal display | PASS |


---

# 9. Security Considerations

This tool is developed strictly for educational purposes.

Packet capturing should only be performed on networks where authorization has been granted.

Unauthorized monitoring of network traffic may violate privacy regulations and security policies.


---

# 10. Limitations

Current limitations:

- No packet storage in PCAP format.
- No graphical dashboard.
- No advanced intrusion detection rules.
- Limited payload inspection.


---

# 11. Future Improvements

Possible improvements:

- Add PCAP file export.
- Integrate threat intelligence APIs.
- Add graphical visualization.
- Implement anomaly detection.
- Add filtering capabilities.


---

# 12. Conclusion

This project provided practical experience in network packet capture, protocol analysis, and cybersecurity monitoring concepts.

The implementation demonstrates the fundamentals of how security analysts inspect network communications and build monitoring tools.
