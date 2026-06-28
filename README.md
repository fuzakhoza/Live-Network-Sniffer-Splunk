# Live-Network-Sniffer-Splunk
## 🛡️ Projects

### 🛠️ Windows 10 Endpoint Hardening & Centralized Splunk SIEM Pipeline
**Technologies Used:** Python 3, Scapy, Splunk Enterprise, Windows Universal Forwarder, Npcap, Windows CLI, Kali Linux, Linux UFW.

Built and deployed a lightweight security monitoring ecosystem designed for resource-constrained endpoints (4GB RAM) running end-of-support operating systems. This project simulates an enterprise-level Security Operations Center (SOC) data ingestion pipeline across a local area network (LAN) hotspot.

#### Key Implementations:
* **Host Hardening:** Disabled vulnerable legacy protocols (SMBv1), optimized User Account Control (UAC) parameters, and established outbound application firewall rules to minimize host vulnerability surfaces.
* **Custom Security Agent:** Engineered a lightweight packet-sniffing program in Python using the Scapy library. The script intercepts raw network traffic on the wireless interface, parses Layer 3 and Layer 4 headers (IP, TCP, UDP, ICMP), and writes structured alerts to a file without causing system lag.
* **Data Log Forwarding:** Deployed and configured the Splunk Universal Forwarder on the Windows host. Created a dedicated monitoring link to stream custom firewall logs to an external receiver in real time.
* **SIEM Indexer Configuration:** Initialized a Splunk Enterprise instance on a remote Kali Linux host. Resolved network communication blocks by auditing the kernel firewall (UFW) and creating dedicated rules to unblock TCP port 9997.
* **Analytical Dashboards:** Formulated structured Splunk Search Processing Language (SPL) queries to filter out local system noise, analyze incoming reconnaissance footprints (Nmap scans), and build traffic protocol visualizations.

---

### 🐛 Vulnerability Research & Bug Bounty Exposure
**Platform:** Bugcrowd (Independent Security Researcher).

* **Validated Discovery:** Successfully identified, documented, and reported a verified technical vulnerability (P5 Triage Accepted) to a corporate program under responsible disclosure guidelines.
* **Reporting Standard:** Authored a technical proof-of-concept (PoC) document outlining exploit vectors, business impact metrics, and systemic mitigation steps for program triage engineers.
