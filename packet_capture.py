# backend/packet_capture.py
from scapy.all import sniff

def capture_packet():
    packets = sniff(count=1)  # Capture 1 packet for demo
    pkt = packets[0]

    # Example features for model
    packet_size = len(pkt)
    protocol = pkt.proto if hasattr(pkt, 'proto') else 0

    return {
        "packet_size": packet_size,
        "protocol": protocol
    }
