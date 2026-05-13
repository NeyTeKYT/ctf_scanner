from modules.web import *
from modules.smb import *
from modules.utils import fatal
from modules.output import create_service_folder, scan_completed
from modules.config import config

def run_web_enumeration(port, resume=False):

    service_folder = create_service_folder(port, "http")
    
    if resume and scan_completed("nikto.txt", port, "http"):
        print(f"[~] Skipping Nikto on port {port}: results already exist")
    else:
        run_nikto(port, service_folder)

    if resume and scan_completed("gobuster.txt", port, "http"):
        print(f"[~] Skipping Gobuster on port {port}: results already exist")
    else:
        run_gobuster(port, service_folder)

    if resume and scan_completed("feroxbuster.txt", port, "http"):
        print(f"[~] Skipping Feroxbuster on port {port}: results already exist")
    else:
        run_feroxbuster(port, service_folder)

    # I need to parse these results to perform actions according to them

def run_smb_enumeration(port, resume):

    service_folder = create_service_folder(port, "smb")

    if resume and scan_completed("enum4linux.txt", port, "smb"):
        print(f"[~] Skipping Enum4Linux on port {port}: results already exist")
        with open(f"{service_folder}/enum4linux.txt") as f:
            enum4linux_scan_result = f.read()
    else:
        enum4linux_scan_result = run_enum4linux(port, service_folder)

    # Parse accessible shares
    shares = parse_enum4linux_shares(enum4linux_scan_result)
    for share in shares:
        answer = input(f"\n[?] Open a shell on share '//{config.target}:{port}/{share}'? (y/n): ")
        if answer.lower() == "y":
            run_smbclient(share)
    
    # Parse existing users for a potential bruteforce attack

def run_enumeration(open_ports, resume=False):

    if not open_ports:
        fatal("\n[!] No open ports to enumerate")

    for port, info in open_ports.items():

        service = info["service"]

        # Check if a web server is running
        if service == "http":
            run_web_enumeration(port, resume)

        # Check if a SMB server is running
        elif service == "netbios-ssn":
            run_smb_enumeration(port, resume)