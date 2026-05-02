import socket
import json
import threading
from datetime import datetime
import time

TARGET_IP = "10.0.2.4"
START_PORT = 1
END_PORT = 1024
OUTPUT_FILE = "scan_report.json"
TIMEOUT = 1.0

scan_results = []
print_lock = threading.Lock()

def grab_banner(s):
    """Attempts to grab the service banner from the open port."""
    try:
        banner = s.recv(1024).decode().strip()
        return banner
    except:
        return "Unknown Service / No Banner"

def scan_port(port):
    """Scans a single port and retrieves service information if open."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        result = s.connect_ex((TARGET_IP, port))
        
        if result == 0:
            banner = grab_banner(s)
            
            with print_lock:
                print(f"[+] Port {port} is OPEN | Service: {banner}")
                
            scan_results.append({
                "port": port,
                "status": "open",
                "service_banner": banner
            })
        s.close()
    except Exception as e:
        pass

def generate_json_report():
    """Saves the scan results to a JSON file."""
    report_data = {
        "target_ip": TARGET_IP,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_open_ports": len(scan_results),
        "results": scan_results
    }
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(report_data, f, indent=4)
    print(f"\n[*] Scan complete. Report successfully saved to {OUTPUT_FILE}")

def main():
    print("-" * 50)
    print(f"[*] Custom Network Scanner Started")
    print(f"[*] Target: {TARGET_IP}")
    print(f"[*] Scanning ports from {START_PORT} to {END_PORT}...")
    print("-" * 50)
    
    start_time = time.time()
    threads = []
    
    for port in range(START_PORT, END_PORT + 1):
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    end_time = time.time()
    print("-" * 50)
    print(f"[*] Total scanning time: {round(end_time - start_time, 2)} seconds")
    
    generate_json_report()

if __name__ == "__main__":
    main()
