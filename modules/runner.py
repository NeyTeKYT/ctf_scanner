from modules.nmap import run_nmap, parse_open_ports
from modules.enumeration import run_enumeration
from modules.output import create_service_folder, scan_completed
from modules.config import config
import os

def resume():
    
    print(f"\n[*] Resuming the CTF completion: already completed commands will be skipped")
    
    # Continue from where the program left off and skip the completed tools
    if scan_completed("nmap.txt"):
        print("\n[+] Skipping Nmap: results already exist")
        with open(f"{config.output_folder}/nmap.txt") as f:
            nmap_result = f.read()
    else:
        nmap_result = run_nmap()
    
    open_ports = parse_open_ports(nmap_result)
    run_enumeration(open_ports, resume=True)

def start():

    print("\n[*] Starting the CTF from scratch!")

    # Run everything from scratch
    nmap_result = run_nmap()
    open_ports = parse_open_ports(nmap_result)
    run_enumeration(open_ports)