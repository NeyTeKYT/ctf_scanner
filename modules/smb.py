from modules.utils import run_command
import re
from modules.config import config

def run_enum4linux(port, folder):
    return run_command(
        ["enum4linux", f"{config.target}:{port}"],
        f"Enum4Linux on the {config.target}:{port} SMB server",
        f"{folder}/enum4linux.txt"
    )

def parse_enum4linux_shares(enum4linux_result):

    shares = []

    for line in enum4linux_result.splitlines():

        # Look for accessible shares
        if "Mapping: OK" in line:
            
            # Extract the share path (for example, //10.128.170.170/Anonymous)
            match = re.search(r'//[\d.]+/(\S+)', line)

            if match:

                # Extract the share name
                share_name = match.group(1)

                shares.append(share_name)  
                print(f"[+] Accessible share found: //{config.target}/{share_name}")
    
    return shares

def run_smbclient(share):
    print(f"\n[*] Opening a SMB shell on //{config.target}/{share}")
    print("[*] Type 'exit' when done to return to the program\n")
    subprocess.run(["smbclient", f"//{config.target}/{share}", "-N"])
    print(f"\n[+] SMB shell closed\n")

def parse_enum4linux_users(enum4linux_result):

    users = []

    # To be completed