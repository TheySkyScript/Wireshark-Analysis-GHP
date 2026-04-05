import pyshark
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("darkgrid")

# Grab execution path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Save function
def save_show(filename):
    plt.savefig(filename)
    print(f"Saved: {filename}")
    plt.show(block=False)
    plt.close()

# Load packet capture data
cap = pyshark.FileCapture(
    BASE_DIR + "/ghp screen capture wireshark.pcap",
    keep_packets=False
)

rows = []

# Extract packet fields for metrics / plots
for pkt in cap:
    rows.append({
        "timestamp": float(pkt.sniff_timestamp),
        "length": int(pkt.length),
        "protocol": pkt.highest_layer,
        "src_ip": pkt.ip.src if hasattr(pkt, "ip") else None,
        "dst_ip": pkt.ip.dst if hasattr(pkt, "ip") else None,
    })
cap.close()

# Create DataFrame
df = pd.DataFrame(rows)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
df.set_index("timestamp", inplace=True)

# Plot 1: Packets over time
plt.figure()
pps = df.resample("1s").size()
plt.plot(pps.index, pps.values)
plt.title("Packets per Second")
plt.xlabel("Time")
plt.ylabel("Packets")
plt.tight_layout()
save_show("packets_per_second.png")

# Plot 2: Bytes per second
plt.figure()
bps = df["length"].resample("1s").sum()
plt.plot(bps.index, bps.values)
plt.title("Bytes per Second")
plt.xlabel("Time")
plt.ylabel("Bytes")
plt.tight_layout()
save_show("bytes_per_second.png")

# Plot 3: Protocol categories
plt.figure()
proto_counts = df["protocol"].value_counts().head(10)
plt.bar(proto_counts.index, proto_counts.values)
plt.title("Top Protocols")
plt.ylabel("Packet Count")
plt.xticks(rotation=45)
plt.tight_layout()
save_show("protocol_distribution.png")

# Plot 4: Packet size distribution
plt.figure()
plt.hist(df["length"], bins=100, log=True)
plt.title("Packet Size Distribution (log scale)")
plt.xlabel("Packet Size (bytes)")
plt.ylabel("Frequency")
plt.tight_layout()
save_show("packet_size_distribution.png")

# Plot 5: Source IP Distribution
plt.figure()
top_src = df["src_ip"].value_counts().head(10)
plt.barh(top_src.index, top_src.values)
plt.title("Top Source IPs")
plt.xlabel("Packet Count")
plt.gca().invert_yaxis()
plt.tight_layout()
save_show("top_source_ips.png")

# Plot 6: Rolling average packets per sec
plt.figure()
rolling_pps = pps.rolling(window=10).mean()
plt.plot(rolling_pps.index, rolling_pps.values)
plt.title("Rolling Avg Packets/sec (10s Window)")
plt.xlabel("Time")
plt.ylabel("Packets/sec")
plt.tight_layout()
save_show("rolling_packets_per_second.png")
