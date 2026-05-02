# Custom Network Vulnerability Scanner & Port Analyzer

## 📌 Project Overview
This project involves the development of a custom, multi-threaded network scanning tool written in Python. Bypassing the reliance on automated tools like Nmap, this script demonstrates a foundational understanding of TCP/IP protocols, socket programming, and automated security reporting.

## 🛠️ Laboratory Environment & Tools
* **Development OS:** Kali Linux (Isolated VM)
* **Target Machine:** Metasploitable 2 (IP: 10.0.2.4)
* **Programming Language:** Python 3.x
* **Core Libraries:** `socket`, `threading`, `json`
* **Virtualization:** Oracle VM VirtualBox

## 💻 Phase 1: Environment Setup & Development
The tool was developed from scratch in an isolated Kali Linux environment. The process began with setting up the workspace and initializing the script via the terminal.

**Commands:** 

`cd Desktop`

`nano scanner.py`

<img width="1407" height="1068" alt="Ekran görüntüsü 2026-05-03 011148" src="https://github.com/user-attachments/assets/fd742ff9-fbb3-49e7-80b7-34a3083088cb" />

Utilizing Python's `socket` library for network connections and `threading` for performance optimization, the core architecture was built to handle multiple ports concurrently.

<img width="1414" height="1067" alt="Ekran görüntüsü 2026-05-03 011000" src="https://github.com/user-attachments/assets/0bd37b83-259b-4a01-a65c-68f46517befb" />

The script also includes custom functions to grab service banners and format the output dynamically, ensuring thread safety with `threading.Lock()`.

<img width="1415" height="1065" alt="Ekran görüntüsü 2026-05-03 011043" src="https://github.com/user-attachments/assets/94e67735-67da-4cdb-b620-2ab70a02f290" />

## 🚀 Phase 2: Execution & Performance
The scanner executes a TCP Connect scan across a specified port range. The implementation of multi-threading significantly reduces the overall scan time.

**Command:** `python3 scanner.py`

<img width="1411" height="1069" alt="Ekran görüntüsü 2026-05-03 011216" src="https://github.com/user-attachments/assets/1a10d2b9-148f-4e2a-888b-ede6e5176fd5" />

**Technical Highlights:**
* **Target Environment:** 10.0.2.4 (Metasploitable 2)
* **Performance:** Scanning 1024 ports completed in just **1.2 seconds**.
* **Banner Grabbing:** Successfully interrogated open ports to capture service banners (e.g., vsFTPd 2.3.4, OpenSSH 4.7p1), which is critical for vulnerability identification.

## 📊 Phase 3: Automated JSON Reporting
Instead of merely printing results to the console, the script is engineered to parse the aggregated scan data and export it into a structured `.json` file. This format is essential for integrating reconnaissance results with other security information and event management (SIEM) tools.

**Command:** `scan_report.json`

<img width="1409" height="1362" alt="Ekran görüntüsü 2026-05-03 011334" src="https://github.com/user-attachments/assets/c2e20202-3edb-43e3-afb3-bd5b65a979ea" />

## 📁 Proof of Work (PoW)
The following directory listing verifies the successful creation of the Python script and its automatically generated JSON output report within the local filesystem.

**Command:** `ls -l`

<img width="1098" height="925" alt="Ekran görüntüsü 2026-05-03 011708" src="https://github.com/user-attachments/assets/0cee2b9b-ea5f-49dc-9423-7f70ff8219bf" />

## 💡 Engineering Takeaways
Developing this scanner from scratch provided deep practical insights into network layer operations. It bridged the gap between theoretical networking concepts and actionable cybersecurity engineering, proving that reliance on pre-compiled penetration testing tools is not a limitation when custom solutions can be engineered to fulfill specific reconnaissance requirements.
