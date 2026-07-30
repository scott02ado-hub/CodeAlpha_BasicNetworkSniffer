"""
packet_analyzer.py
-----------------
Analyze captured network packets.

Author: Scott
Project: CodeAlpha Basic Network Sniffer
"""

from datetime import datetime
from scapy.packet import Packet
from scapy.layers.inet import IP, TCP, UDP, ICMP


class PacketAnalyzer:
    """
    Extract useful information from network packets.
    """

    def analyze(self, packet: Packet) -> dict:
        """
        Analyze a Scapy packet.

        Args:
            packet (Packet): Captured network packet.

        Returns:
            dict: Extracted packet information.
        """

        packet_info = {
            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "length": len(packet),
            "protocol": "Unknown"
        }

        # Check IP layer
        if packet.haslayer(IP):

            packet_info["source_ip"] = packet[IP].src
            packet_info["destination_ip"] = packet[IP].dst

            # Detect transport protocol

            if packet.haslayer(TCP):
                packet_info["protocol"] = "TCP"

                packet_info["source_port"] = (
                    packet[TCP].sport
                )

                packet_info["destination_port"] = (
                    packet[TCP].dport
                )

            elif packet.haslayer(UDP):
                packet_info["protocol"] = "UDP"

                packet_info["source_port"] = (
                    packet[UDP].sport
                )

                packet_info["destination_port"] = (
                    packet[UDP].dport
                )

            elif packet.haslayer(ICMP):
                packet_info["protocol"] = "ICMP"

        return packet_info
