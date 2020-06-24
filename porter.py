from termcolor import colored

import socket
import sys

def help():
    print(colored("--------------------------------------", "red"))
    print(colored("  ____   ___  ____ _____ _____ ____   ", "green"))
    print(colored(" |  _ \ / _ \|  _ \_   _| ____|  _ \  ", "green"))
    print(colored(" | |_) | | | | |_) || | |  _| | |_) | ", "green"))
    print(colored(" |  __/| |_| |  _ < | | | |___|  _ <  ", "green"))
    print(colored(" |_|    \___/|_| \_\|_| |_____|_| \_\ ", "green"))
    print(colored("--------------------------------------", "red"))
    print()
    print("Usage: python porter.py [Target IP] [Options]")
    print()
    print("-h, --help  --> show this window")
    print("-a, --all   --> show close and open ports")
    print("-o, --open  --> show only open ports")
    print("-c, --close --> show only closed ports")
    print()
    print("Example: python porter.py 8.8.8.8 --all")
    
def main(ip, mode):
    scanner = socket.socket()

    for i in range(65536):
        try:
            scanner.connect((ip, i))
        except OSError:
            if (((mode == "-a") or (mode == "-c")) or ((mode == "--all") or (mode == "--close"))):
                print(colored("[!]", "red") + " PORT " + str(i) + " CLOSED")
        else:
            if (((mode == "-a") or (mode == "-o")) or ((mode == "--all") or (mode == "--open"))):
                print(colored("[!]", "yellow") + " PORT " + str(i) + " OPEN")
    
if __name__=="__main__":
    try:
        if ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
            help()
        else:
            main(sys.argv[1], sys.argv[2])
    except IndexError:
        help()