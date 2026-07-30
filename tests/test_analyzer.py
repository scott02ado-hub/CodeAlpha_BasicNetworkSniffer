import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from scapy.layers.inet import IP, TCP
from scapy.packet import Raw

from src.packet_analyzer import PacketAnalyzer


# Création d'un paquet fictif
packet = (
    IP(
        src="192.168.1.10",
        dst="8.8.8.8"
    )
    /
    TCP(
        sport=12345,
        dport=443
    )
    /
    Raw(load="Hello Network")
)


analyzer = PacketAnalyzer()

result = analyzer.analyze(packet)


print(result)
