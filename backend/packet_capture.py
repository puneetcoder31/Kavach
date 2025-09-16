# backend/packet_capture.py
import random
import time

import random
  
def capture_fake_packet():
    labels = ["normal", "malicious", "ddos"]
    flags = ["SYN","ACK","FIN","PSH","RST"]
    protocols = ["TCP","UDP","ICMP"]

    pkt = {
        "src_ip": f"192.168.1.{random.randint(1,254)}",
        "dst_ip": f"10.0.0.{random.randint(1,254)}",
        "src_port": random.randint(1024,65535),
        "dst_port": random.randint(1,1024),
        "protocol": random.choice(protocols),
        "flag": random.choice(flags),
        "raw": "some_data",
        "label": random.choice(labels)  # randomly normal/malicious/ddos
    }
    return pkt

