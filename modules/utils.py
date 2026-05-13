import argparse
import subprocess
from modules.output import save_result
from modules.config import config

def parse_arguments():
    
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Automated CTF Scanning & Enumeration Tool",
        epilog="Examples:\n python3 main.py 10.128.170.170\n python3 main.py -v 10.128.189.38",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-v", "--verbose", action="store_true", help="Also print the results in the terminal (results are always saved in files)")

    args = parser.parse_args()
    return args.target, args.verbose

def print_result(message):
    if config.verbose:
        print(message)

def fatal(message):
    print(message)
    exit(0)

def run_command(command, label, filepath):

    print(f"[*] Running {label}...")

    result = subprocess.run(command, text=True, capture_output=True)
    
    if result.stdout:

        print_result(result.stdout)
        
        if filepath:
            save_result(result.stdout, filepath)
    
    return result.stdout