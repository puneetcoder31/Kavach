from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Store logs in memory
logs = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/packets')
def packets():
    # Generate a new packet every request
    packet_type = random.choice(["Normal", "Malicious"])
    packet = {
        "timestamp": time.strftime("%H:%M:%S"),
        "src_ip": f"192.168.1.{random.randint(2, 254)}",
        "dst_ip": f"10.0.0.{random.randint(2, 254)}",
        "protocol": random.choice(["TCP", "UDP", "ICMP"]),
        "port": random.randint(1000, 9999),
        "status": packet_type
    }
    logs.append(packet)
    if len(logs) > 20:  # keep only last 20 logs
        logs.pop(0)

    # Count packets
    normal_count = sum(1 for l in logs if l["status"] == "Normal")
    malicious_count = sum(1 for l in logs if l["status"] == "Malicious")

    return jsonify({"logs": logs, "normal": normal_count, "malicious": malicious_count})

if __name__ == '__main__':
    app.run(debug=True)
