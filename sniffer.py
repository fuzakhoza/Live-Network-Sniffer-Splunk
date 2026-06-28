import os
import logging
from scapy.all import sniff, IP, TCP, UDP

# 1. CREATE DIRECTORY FOR SPLUNK INGESTION
log_dir = "C:\\SecurityLogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 2. CONFIGURE SPLUNK-FRIENDLY KEY-VALUE PAIR LOGGING
logging.basicConfig(
    filename=os.path.join(log_dir, "py_firewall.log"), 
    level=logging.INFO,
    format="%(asctime)s | SRC=%(message)s"
)

# 3. PACKET PROCESSING LOGIC
def analyze_packet(pkt):
    if pkt.haslayer(IP):
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        
        # Parse Layer 4 Protocols
        proto = "OTHER"
        dport = "NONE"
        if pkt.haslayer(TCP):
            proto = "TCP"
            dport = pkt[TCP].dport
        elif pkt.haslayer(UDP):
            proto = "UDP"
            dport = pkt[UDP].dport
            
        # Format logs as structured text strings
        log_entry = f"{src_ip} DST={dst_ip} PROTO={proto} DPORT={dport}"
        
        # Print alerts live to the terminal screen
        print(f"[!] Traffic Detected: {log_entry}")
        
        # Commit the string entry to disk for the Splunk Forwarder to read
        logging.info(log_entry)

# 4. INITIALIZE RECOVERY INTERCEPT LOOPS
print("[+] Python Sniffer Shield Active... Monitoring Wi-Fi packets.")
print("[+] Press Ctrl+C to exit safely.")

# Capture live IP traffic without overloading system RAM
sniff(filter="ip", prn=analyze_packet, store=0)
