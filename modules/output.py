import os
from modules.config import config

folder_exists = False

def ask_ctf_name():

    while True:
        ctf_name = input("[?] Enter the CTF name (e.g. Basic_Pentesting): ").strip()
        if not ctf_name:
            print("[!] The CTF name cannot be empty: It will be part of the folder name containing the results!\n")
            continue
        if " " in ctf_name:
            print("[!] Use underscores instead of spaces (e.g. Basic_Pentesting)\n")
            continue
        break

    return ctf_name

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    return path

def find_existing_ctf_name_folders(ctf_name):

    if not os.path.exists("results"):
        return []

    # Return all existing folders matching [CTF_NAME]_[any IP address] in results/
    return [
        d for d in os.listdir("results")
        if d.startswith(ctf_name + "_") and os.path.isdir(f"results/{d}")
    ]

def ask_fresh_start():

    while True:
        answer = input(f"\n[?] Do you want to start fresh for the new target? (y/n): ").strip().lower()
        if answer != "y" and answer != "n":
            print("[!] Only allowed answers are 'y' and 'n' !\n")
            continue
        break

    return answer

def verifying_folder(folder, ctf_name):

    global folder_exists

    # Check if the CTF name and IP address are the same
    if os.path.exists(folder):

        # Resuming where the program left off
        folder_exists = True
        print(f"\n[+] Found existing results for '{ctf_name}' on {config.target} in {folder}")
        return

    # Same CTF name but different IP
    existing = find_existing_ctf_name_folders(ctf_name)

    if existing:
        previous_ip = existing[0].replace(ctf_name + "_", "")
        print(f"\n[+] Found existing results for '{ctf_name}' on a different target: {previous_ip} in {folder}")
        
        fresh_start = ask_fresh_start()

        if not answer:
            fatal("Exiting: no changes to be made")

    # Brand new CTF or confirmed fresh start
    folder_exists = False
    print(f"[+] Starting new CTF: '{ctf_name}' on {config.target}")

def create_output_folder():

    ctf_name = ask_ctf_name()

    folder = f"results/{ctf_name}_{config.target}"

    verifying_folder(folder, ctf_name)

    create_folder(folder)

    return folder

def create_service_folder(port, service):
    return create_folder(f"{config.output_folder}/{port}_{service}")

def save_result(content, filepath):

    if not config.output_folder:
        config.output_folder = create_output_folder()
    
    with open(filepath, "w") as f:
        f.write(content)
    
    print(f"[+] Results saved to {filepath}")