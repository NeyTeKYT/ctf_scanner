from modules.utils import run_command, print_log
import re
from modules.config import config

def run_nmap():
    return run_command(
        ["nmap", "-sS", "-sV", config.target],
        f"Nmap to find open services and basic information about the target",
        f"{config.output_folder}/nmap.txt"
    )

def parse_open_ports(nmap_result):

    open_ports = {}

    for line in nmap_result.splitlines():

        # Look for open ports lines
        match = re.search(r'(\d+)/(tcp|udp)\s+open\s+(\S+)\s*(.*)', line)

        if match:

            port = int(match.group(1))
            proto = match.group(2)
            service = match.group(3)
            version = match.group(4).strip()

            open_ports[port] = {
                "proto": proto,
                "service": service,
                "version": version
            }

            print_log(
                f"[+] Open port found: "
                f"{f'{port}/{proto}':<10} "
                f"Service: {service:<15} "
                f"Version: {version or 'unknown'}"
            )

    return open_ports