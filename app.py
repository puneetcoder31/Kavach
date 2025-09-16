from flask import Flask, render_template, Response, request
import pandas as pd
import json
import time
import random

app = Flask(__name__)

# Streaming control
streaming = False

# Simulate LabelEncoder for protocol & flag (simple mapping)
le_protocol = {"TCP":0, "UDP":1, "ICMP":2}
le_flag = {"SYN":0, "ACK":1, "FIN":2, "RST":3, "PSH":4, "URG":5}  # include common flags

# Function to generate fake packets
def capture_fake_packet():
    labels = ["normal", "malicious", "ddos"]
    protocols = list(le_protocol.keys())
    flags = list(le_flag.keys())
    pkt = {
        "src_ip": f"192.168.1.{random.randint(1,254)}",
        "dst_ip": f"10.0.0.{random.randint(1,254)}",
        "src_port": random.randint(1024,65535),
        "dst_port": random.randint(20,1024),
        "protocol": random.choice(protocols),
        "flag": random.choice(flags),
        "raw": random.randint(50,1500),
        "label": random.choices(labels, weights=[0.6,0.25,0.15])[0]  # more normal, some malicious/ddos
    }
    return pkt

# Streaming generator
def generate_packets():
    global streaming
    while streaming:
        pkt = capture_fake_packet()
        # Encode protocol and flag safely
        proto_encoded = le_protocol.get(pkt["protocol"], 0)
        flag_encoded = le_flag.get(pkt["flag"], 0)
        df = pd.DataFrame([{
            "src_port": pkt["src_port"],
            "dst_port": pkt["dst_port"],
            "protocol": proto_encoded,
            "flag": flag_encoded,
            "raw": pkt["raw"]
        }])
        # Normally here you would predict using a model
        # pkt["label"] already has normal/malicious/ddos
        yield f"data: {json.dumps(pkt)}\n\n"
        time.sleep(1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    return Response(generate_packets(), mimetype="text/event-stream")

@app.route("/start_stream", methods=["POST"])
def start_stream():
    global streaming
    streaming = True
    return {"status":"started"}

@app.route("/stop_stream", methods=["POST"])
def stop_stream():
    global streaming
    streaming = False
    return {"status":"stopped"}

if __name__ == "__main__":
    app.run(debug=True)
