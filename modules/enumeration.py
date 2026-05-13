from modules.web import *
from modules.smb import *
from modules.utils import fatal
from modules.output import create_service_folder
from modules.config import config

def run_web_enumeration(port):

    service_folder = create_service_folder(port, "http")
    
    nikto_result = run_nikto(port, service_folder)
    gobuster_result = run_gobuster(port, service_folder)
    feroxbuster_result = run_feroxbuster(port, service_folder)

    # I need to parse these results to perform actions according to them

def run_smb_enumeration(port):

    service_folder = create_service_folder(port, "smb")

    enum4linux_scan_result = run_enum4linux(port, service_folder)

    # Parse accessible shares
    shares = parse_enum4linux_shares(enum4linux_scan_result)
    for share in shares:
        answer = input(f"\n[?] Open a shell on share '//{config.target}:{port}/{share}'? (y/n): ")
        if answer.lower() == "y":
            run_smbclient(share)
    
    # Parse existing users for a potential bruteforce attack

def run_enumeration(open_ports):

    if not open_ports:
        fatal("[!] No open ports to enumerate")

    for port, info in open_ports.items():

        service = info["service"]

        # Check if a web server is running
        if service == "http":
            run_web_enumeration(port)

        # Check if a SMB server is running
        elif service == "netbios-ssn":
            run_smb_enumeration(port)