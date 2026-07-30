"""
network_sniffer.py
-----------------
Capture network packets using Scapy.

Author: Scott
Project: CodeAlpha Basic Network Sniffer
"""

from scapy.all import sniff
from scapy.error import Scapy_Exception

from src.packet_analyzer import PacketAnalyzer
from src.logger import get_logger
from src.display import PacketDisplay


class NetworkSniffer:
    """
    Main packet capture engine.
    """

    def __init__(self, interface: str):
        """
        Initialize the network sniffer.

        Args:
            interface (str): Network interface name.
        """

        self.interface = interface
        self.analyzer = PacketAnalyzer()
        self.logger = get_logger()
        self.display = PacketDisplay()
        self.packet_count = 0


    def process_packet(self, packet):
        """
        Process each captured packet.

        Args:
            packet: Scapy packet object.
        """

        self.packet_count += 1

        packet_info = self.analyzer.analyze(packet)

        # Display packet in terminal
        self.display.show_packet(packet_info)

        # Save packet information in log file
        self.logger.info(
            f"Packet #{self.packet_count} | {packet_info}"
        )


    def start(self):
        """
        Start packet capture.
        """

        self.display.show_banner()

        self.logger.info(
            f"Starting capture on {self.interface}"
        )

        try:
            sniff(
                iface=self.interface,
                prn=self.process_packet,
                store=False
            )

        except KeyboardInterrupt:

            self.logger.info(
                "Stopping sniffer..."
            )

            self.logger.info(
                f"Total packets captured: {self.packet_count}"
            )

        except Scapy_Exception as error:

            self.logger.error(
                f"Scapy error: {error}"
            )
