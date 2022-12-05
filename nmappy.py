'''
nmappy python nmap tool
'''

import nmap

print("\nEnter the information you would like to scan with. For help type \"help\"\n")


def helport():
	what_ports = input(f'PORT / PORT RANGE:\n\t>>')
	if what_ports == "help":
		print("Enter the port / ports you would like to scan: (ex. 23, 23-200)")
		helport()

def helpip():
	what_ip = input(f'IP:\n\t>>')
	if what_ip == "help":
		print("Enter the ip address for which you would like to scan: (ex. 8.8.8.8)")
		helpip()

def helpopt():
	what_options = input(f'NMAP OPTIONS:\n\t>>')
	if what_options == "help":
		print("Enter the additional opetions you would like to apply to your scan: (ex. -sL)")
		helpopt()

what_ip = helpip()
what_ports = helport()
what_options = helpopt()

nm = nmap.PortScanner()

new_scan = nm.scan(what_ip, what_ports)
print(new_scan)


#initiate scan


#print output