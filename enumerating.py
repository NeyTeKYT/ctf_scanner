#       How to execute the program:
#       "python3 enumerating.py [IP_ADDRESS]"

import sys
import subprocess

def nmap(ip_address):
        nmap = subprocess.run(["nmap", "-sS", "-sV", ip_address], capture_output=True, text=True)
        # Stocker le résultat dans un fichier "nmap_[IP_ADDRESS].txt"
        print(nmap.stdout)
        return nmap.stdout      # Retourne le résultat du scan Nmap

# Parsing des ports ouverts détectés
def open_ports(scan_nmap):
        open_ports = []
        for line in scan_nmap.split("\n"):
                if "open" in line:
                        port = line.split("/")[0]
                        open_ports.append(port)
        return open_ports

def gobuster(ip_address):

        # Scan Gobuster si le port 80 est ouvert
        if "80" in open_ports:
                gobuster = subprocess.run(["gobuster", "dir", "-u", ip_address, "-w",
                "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"])
                print(gobuster.stdout)


# Fonction qui effectue différentes actions en fonction des ports ouverts détectés
def open_ports_scanning(open_ports, ip_address):

        # Scan Gobuster si le port 80 est ouvert
        if "80" in open_ports:
                gobuster(ip_address)

        # Scan enum4linux et test avec smbclient si le port smb est ouvert
        # À COMPLÉTER

        # Bruteforce SSH avec Paramiko SI le port 22 est ouvert
        # À COMPLÉTER

if __name__ == '__main__':

        # Vérifie que le script a bien été appelé avec un seul argument : l'adresse IP de la target
        if len(sys.argv) != 2:
                sys.exit(1)

        ip_address = sys.argv[1]        # Stockage de l'adresse IP de la target dans une variable

        scan_nmap = nmap(ip_address)    # Scan NMAP

        open_ports = open_ports(scan_nmap)      # Tableau contenant tous les ports ouverts détectés

       	open_ports_scanning(open_ports, ip_address)     # Scans en fonction des ports ouverts détectés
