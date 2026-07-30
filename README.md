# CodeAlpha Basic Network Sniffer

A Python-based network packet analyzer developed as part of the CodeAlpha Cyber Security Internship.

This project demonstrates the fundamentals of network traffic monitoring, packet capture, and protocol analysis using Python and Scapy.

---

##  Project Overview

The **Basic Network Sniffer** is a cybersecurity tool designed to capture live network packets from a selected network interface and analyze their structure.

The application helps understand how data flows through a network by displaying important packet information such as:

- Source IP address
- Destination IP address
- Protocol type
- Source and destination ports
- Packet size
- Capture timestamp

---

##  Features

✅ Live network packet capture 
✅ TCP / UDP protocol identification 
✅ Source and destination IP extraction 
✅ Port analysis 
✅ Packet size monitoring 
✅ Real-time terminal visualization 
✅ Structured logging system 
✅ Modular Python architecture 
✅ Graceful shutdown handling 

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Scapy | Packet capture and network analysis |
| Rich | Professional terminal interface |
| Colorama | Terminal formatting |
| Git | Version control |

---

## 📂 Project Structure
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── src/
│ ├── network_sniffer.py
│ ├── packet_analyzer.py
│ ├── display.py
│ ├── logger.py
│ └── utils.py
│
├── logs/
│ └── capture.log
│
├── tests/
│ └── test_analyzer.py
│
├── screenshots/
│
└── report/


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git

### 2. Enter project directory
cd CodeAlpha_BasicNetworkSniffer

### 3. Create virtual environment
python3 -m venv .venv

### 4. Activate environment

Linux:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

### 5. Install dependencies
pip install -r requirements.txt

#Usage

Network packet capture requires administrator privileges.

Linux:

sudo .venv/bin/python main.py

The application will start capturing packets from the configured network interface.

#Example:

CODEALPHA NETWORK SNIFFER

Captured Packet

Protocol       TCP
Source         104.18.39.21:443
Destination    10.1.5.82:32818
Size           66 bytes

### Testing

Run packet analyzer test:

python3 tests/test_analyzer.py

Expected output:

Packet analysis completed successfully

### Security Notes

This project is developed for educational purposes.

The tool should only be used on networks where you have explicit authorization to monitor traffic.

Unauthorized packet interception may violate privacy laws and security policies.

### Screenshots

Screenshots demonstrating packet capture will be added in:

/screenshots

# Author
ADOGNON Komlan Dosseh Aimé
# Cyber Security Internship Project
CodeAlpha
