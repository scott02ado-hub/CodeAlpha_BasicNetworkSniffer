"""
display.py
----------
Professional terminal output.

Author: Scott
Project: CodeAlpha Basic Network Sniffer
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


class PacketDisplay:
    """
    Display captured packets in terminal.
    """

    def show_banner(self):
        """
        Display application banner.
        """

        console.print(
            Panel(
                "[bold cyan]CODEALPHA NETWORK SNIFFER[/bold cyan]\n"
                "Basic Python Packet Analyzer",
                title="Cyber Security Project"
            )
        )


    def show_packet(self, packet_info: dict):
        """
        Display packet information.

        Args:
            packet_info (dict): Analyzed packet.
        """

        table = Table(
            title="Captured Packet"
        )

        table.add_column(
            "Field"
        )

        table.add_column(
            "Value"
        )


        table.add_row(
            "Protocol",
            packet_info.get(
                "protocol",
                "Unknown"
            )
        )

        table.add_row(
            "Source",
            f"{packet_info.get('source_ip', 'N/A')}:"
            f"{packet_info.get('source_port', '-')}"
        )

        table.add_row(
            "Destination",
            f"{packet_info.get('destination_ip', 'N/A')}:"
            f"{packet_info.get('destination_port', '-')}"
        )

        table.add_row(
            "Size",
            f"{packet_info.get('length')} bytes"
        )


        console.print(table)
