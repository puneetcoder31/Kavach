import random
import pandas as pd

def generate_fake_packets(n=55):
    data = []
    for i in range(n):
        packet = {
            "src_ip": f"192.168.1.{random.randint(1, 255)}",
            "dst_ip": f"10.0.0.{random.randint(1, 255)}",
            "src_port": random.randint(1024, 65535),
            "dst_port": random.randint(20, 1024),
            "protocol": random.choice(["TCP", "UDP", "ICMP"]),
            "flag": random.choice(["SYN", "ACK", "FIN", "RST"]),
            "raw": random.randint(50, 1500),   # packet size
            "label": "normal"
        }

        # Inject some malicious & ddos
        if 35 < i < 45:
            packet["label"] = "malicious"
        elif i >= 45:
            packet["label"] = "ddos"

        data.append(packet)

    df = pd.DataFrame(data)
    df.to_csv("packets.csv", index=False)
    print("[+] Fake packet data saved as packets.csv")

if __name__ == "__main__":
    generate_fake_packets()
