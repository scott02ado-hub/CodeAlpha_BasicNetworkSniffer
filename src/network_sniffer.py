"""
network_sniffer.py
-----------------
Capture network packets using Scapy.

Author: Scott
Project: CodeAlpha Basic Network Sniffer
"""

from scapy.all import sniff

from src.packet_analyzer import PacketAnalyzer
from src.logger import get_logger


class NetworkSniffer:
    """
    Main packet capture engine.
    """

    def __init__(self, interface: str):
        """
        Initialize sniffer.

        Args:
            interface (str): Network interface name.
        """

        self.interface = interface
        self.analyzer = PacketAnalyzer()
        self.logger = get_logger()

        self.packet_count = 0


    def process_packet(self, packet):
        """
        Process each captured packet.

        Args:
            packet: Scapy packet object.
        """

        self.packet_count += 1

        packet_info = self.analyzer.analyze(packet)

        self.logger.info(
            f"Packet #{self.packet_count} | "
            f"{packet_info}"
        )


    def start(self):
        """
        Start packet capture.
        """

        self.logger.info(
            f"Starting capture on {self.interface}"
        )

        sniff(
            iface=self.interface,
            prn=self.process_packet,
            store=False
        )
