from modules.utils import run_command
from modules.config import config

def run_nikto(port, folder):
    return run_command(
        ["nikto", "-host", f"{config.target}:{port}"],
        f"Nikto on the {config.target} web server",
        f"{folder}/nikto.txt"
    )

def run_gobuster(port, folder):
    return run_command(
        ["gobuster", "dir", "-u", f"{config.target}:{port}", "-w", "/usr/share/wordlists/dirb/common.txt"],
        f"Gobuster on the {config.target} web server",
        f"{folder}/gobuster.txt"
    )

def run_feroxbuster(port, folder):
    return run_command(
        ["feroxbuster", "-u", f"http://{config.target}:{port}"],
        f"Feroxbuster on the {config.target} web server",
        f"{folder}/feroxbuster.txt"
    )