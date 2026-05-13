# runner.py
from modules.nmap import run_nmap, parse_open_ports
from modules.enumeration import run_enumeration
from modules.output import create_service_folder
from modules.config import config
import os

def scan_completed(filename):

    # Check if a tool has already produced a non-empty result file
    filepath = f"{config.output_folder}/{filename}"
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0

def resume():
    
    print(f"\n[*] Resuming the CTF completion: already completed scans will be skipped")
    
    # Continue from where the program left off and skip the completed tools
    if scan_completed("nmap.txt"):
        print("\n[~] Skipping Nmap: results already exist")
        with open(f"{config.output_folder}/nmap.txt") as f:
            nmap_result = f.read()
    else:
        nmap_result = run_nmap()
    
    open_ports = parse_open_ports(nmap_result)
    run_enumeration(open_ports)

def start():

    print("\n[*] Starting the CTF from scratch!\n")

    # Run everything from scratch
    nmap_result = run_nmap()
    open_ports = parse_open_ports(nmap_result)
    run_enumeration(open_ports)