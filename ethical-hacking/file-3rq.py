import nmap

def network_scan(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, '1-1024')

    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print(f'State: {nm[host].state()}')

        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')

            lport = nm[host][proto].keys()
            for port in lport:
                print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')

target_ip = '192.168.1.1'
network_scan(target_ip)