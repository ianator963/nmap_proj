'''
nmappy python nmap tool
'''

import nmap

print("<options>")

what_ports = input(f'PORT / PORT RANGE:\n\t>>')
what_ip = input(f'IP:\n\t>>')
what_options = input(f'NMAP OPTIONS:\n\t>>')

nm = nmap.PortScanner()

new_scan = nm.scan(what_ip, what_ports)
print(new_scan)


#initiate scan


#print output