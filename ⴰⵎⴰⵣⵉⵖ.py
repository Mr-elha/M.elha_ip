from art import *
import socket
import os
import time
import requests

W = '\33[97;1m'
R = '\33[91;1m'
G = '\33[92;1m'
Y = '\33[93;1m'
B = '\33[94;1m'
P = '\33[95;1m'
C = '\33[96;1m'
N = '\33[0m'

print(G+'______________LIBRARY_____________')
print('')
os.system('pip install art')
os.system('pip install socket')
os.system('pip install time')
os.system('pip install requests')
print(G+'______________the end_______________')
time.sleep(2)
os.system('clear')
 #Text colors
W = '\33[97;1m'
R = '\33[91;1m'
G = '\33[92;1m'
Y = '\33[93;1m'
B = '\33[94;1m'
P = '\33[95;1m'
C = '\33[96;1m'
N = '\33[0m'

logo = '''

'\033[1m'
╔══ ⵣⵣⵣⵣⵣⵣ              ⵣⵣⵣⵣⵣⵣ
╚╣╠╝     ⵣ   AMAZIGH    ⵣ
─║║╔══╗  ⵣ              ⵣ           ∆
─║║║╔╗║ⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣ   {° °}
╔╣╠╣╚╝║  ⵣ     By M.ELH ⵣ   ---- / <°> \ _____
╚══╣═╝   ⵣ              ⵣ        |  ?  |
── ⵣⵣⵣⵣⵣⵣⵣ              ⵣⵣⵣⵣⵣⵣ   _______
───                               ¥   ¥
'''
print(R+logo)


def scan_ports(ip, num_ports):
    open_ports = []
    for port in range(1, num_ports + 1):  # Scan the specified ports from 1 to num_ports
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports
def get_ip_address():
   
    website = input(R+"Enter the site name: ")
    
    ip_address = socket.gethostbyname(website)
    time.sleep(2)
    print('')
    print(G+"\tThe IP address of the website is:", G + ip_address + N)

# User choice
print('\33[96mⴰⵎⴰⵣⵉⵖ'*10)
print( G+'ⴰⵎⴰⵣⵉⵖ'*10)
print( Y+'ⴰⵎⴰⵣⵉⵖ'*10)
print('')
print("\t\033[97;1m[\033[92;1m1\033[97;1m] \033[0;93mIP SCAN")
print("\t\033[97;1m[\033[92;1m2\033[97;1m] \033[0;93mGET WEBSITE IP")
print("\t\033[97;1m[\033[92;1m3\033[97;1m] \033[0;93mURL SCAN")
print('')
choice = input(G + "Choose a number: ")
print('\33[96mⴰⵎⴰⵣⵉⵖ'*10)
print( G+'ⴰⵎⴰⵣⵉⵖ'*10)
print( Y+'ⴰⵎⴰⵣⵉⵖ'*10)
time.sleep(3)
os.system('clear')
# Perform the appropriate task based on user choice
def print_amazigh_banner():
    banner = """

╔══╗
╚╣╠╝ⵣ       ⵣ
─║║╔══╗  ⵣ
─║║║╔╗║ⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣⵣ
╔╣╠╣╚╝║  ⵣ
╚══╣╔═╝  ⵣ
───║║
───╚╝ⵣ
    """
    print(banner)

# استدعاء الدالة لطباعة البانر
print_amazigh_banner()
if choice == "1":
    
    ip_address = input(R + "Enter the IP address you want to scan: ")
    num_ports = int(input(B+"Enter the number of ports: "))
    open_ports = scan_ports(ip_address, num_ports)
    if len(open_ports) > 0:
        print(G+"Open ports on", ip_address, "are:")
        for port in open_ports:
            print(str(port) + N)
    else:
        print(R+"There are no open ports on", ip_address)
elif choice == "2":
    get_ip_address()

 
if choice == "3":
    def check_url_security(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(G+"\t\tThe link is secure \nThe link is secure"*3)
            else:
                print(R+"\t\tThe link is not secure"*10)
        except requests.exceptions.RequestException as e:
            print("An error occurred while trying to connect to the address URL :", str(e))

    # قم بتحديد العنوان URL الذي ترغب في فحصه
    url = input('INTER URL : ')

    # قم بفحص العنوان URL
    check_url_security(url)