import socket
import sys
import os

try:
    from termcolor import colored
except ModuleNotFoundError:
    os.system("pip install termcolor")

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
    print("-h, --help        --> show this window")
    print("-a, --all         --> show close and open ports")
    print("-o, --open        --> show only open ports")
    print("-c, --close       --> show only closed ports")
    print("-p, --port <port> --> scan only one port")
    print()
    print("Example: python porter.py 8.8.8.8 --all")
    
def main(ip, mode, port = None):
    scanner = socket.socket()

    if (port == None):
        for i in range(65536):
            try:
                scanner.connect((ip, i))
            except OSError:
                if (((mode == "-a") or (mode == "-c")) or ((mode == "--all") or (mode == "--close"))):
                    print(colored("[!]", "red") + " PORT " + str(i) + " CLOSED")
            else:
                if (((mode == "-a") or (mode == "-o")) or ((mode == "--all") or (mode == "--open"))):
                    print(colored("[!]", "yellow") + " PORT " + str(i) + " OPEN")
    else:
        try:
            scanner.connect((ip, port))
        except OSError:
            if (((mode == "-a") or (mode == "-c")) or ((mode == "--all") or (mode == "--close"))):
                print(colored("[!]", "red") + " PORT " + str(port) + " CLOSED")
        else:
            if (((mode == "-a") or (mode == "-o")) or ((mode == "--all") or (mode == "--open"))):
                print(colored("[!]", "yellow") + " PORT " + str(port) + " OPEN")
    
if __name__=="__main__":
    try:
        if (len(sys.argv) <= 3):
            if ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
                help()
            else:
                main(sys.argv[1], sys.argv[2])
        else:
            if ((sys.argv[2] == "-p") or (sys.argv[2] == "--port")):
                try:
                    port = int(sys.argv[3])
                except ValueError:
                    print("Invalid port")
                    exit()
                main(sys.argv[1], sys.argv[4], port)
            elif ((sys.argv[3] == "-p") or (sys.argv[3] == "--port")):
                try:
                    port = int(sys.argv[4])
                except ValueError:
                    print("Invalid port")
                    exit()
                main(sys.argv[1], sys.argv[2], port)
            else:
                help()
    except IndexError:
        help()
