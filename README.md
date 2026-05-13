# CTF_Scanner

CTF_Scanner is an automated scanning and enumeration tool. It is intended as a time-saving tool for use in CTFs.  

The tool works by firstly performing a port scans / service detection scans with nmap. From those results, the tool will launch further enumeration scans of those services using a number of different tools. For example, if HTTP is found, then nikto will be launched as well as many others.  

The author will not be held responsible for negative actions that result for te mis-use of this tool.

## Origin

CTF_Scanner was firstly imagined by a LinkedIn comment on one of my posts, where someone has suggested me to automate scanning targets with a script instead of re-running the same commands again and again.  

Besides, I've kept in mind what one of my computer science degree teacher has told me: "if you run a command once, it's ok; twice it starts to be boring; thrice just do a program to automate it" and this was exactly my mindset when I've thought of this project.

Then, CTF_Scanner has implemented some features ideas from AutoRecon which is a similar tool but far more complete than mine.  

Finally, after having participated to a CTF IRL, easy challenges where really obvious, for instance I remember collecting the flag as a comment in the page source. That would be the goal of my tool, to retrieve easy flags easily and without loosing time to focus on the hard one. However, since the goal is to learn after all, I'm going to try making a tool for everyone, even beginners by adding messages when running the program to help the user understand what the program is doing and why it's doing what it's doing.

## Features 

- Supports only IPv4 addresses.
- Lets the user decide whether he wants to print the tools results in the terminal or not (it will be written in files anyway).
- According to the name of the directory `[CTF_NAME]_[TARGET IP]`, the program can resume the former launch where the program left off or start fresh with a brand new directory from the beginning.
- Results will be stored in a similar directory, for corresponding tools results on a certain service, they will be stored in a sub-directory like `[PORT]_[SERVICE]` where service can be http, smb, etc.

## Usage

CTF_Scanner was programmed in Python, with the python3 version.

```
usage: main.py [-h] [-v] target

Automated CTF Scanning & Enumeration Tool

positional arguments:
  target         Target IP address

options:
  -h, --help     show this help message and exit
  -v, --verbose  Also print the results in the terminal (results are always saved in files)

Examples:
 python3 main.py 10.128.170.170
 python3 main.py -v 10.128.189.38
```

## Results 

Results will be stored in the `ctf_scanner/results` directory (it will be created if it's not existing yet). Then, a question will be asked to the user to return the CTF name to formate the sub directory with this format : `[CTF_NAME]_[TARGET IP]`, such as `Basic_Pentesting_10.10.10.10`.  

Keep in mind that if the directory has already been created, so the program will run as a resume mode and will continue where it left off, where results are missing. This allows the program to re-use the convenient and already generated results.  

Secondly, after the nmap scan, if for example a http service has been discovered on the port 80, then it will create a sub-directory as `ctf_scanner/results/[CTF_NAME]_[TARGET IP]/[port]_[service]` containing the specific tools results. This allows the user to focus on only one service like the web server.

## Improvements ideas

- A colorized printage in the terminal for distinguishing separate pieces of information.
- Writting a README.md file containing the findings and complex actions that could be done after having founded vulnerabilities on the target. It could be considered as the documentation phase of a pentest.
- Add a file containing the run commands to improve the resume mode for a better maintenability.
- Add arguments to prevent the program asking the user some information like the CTF_NAME or even if he wants or not to open shells like a SMB shell with smbclient.