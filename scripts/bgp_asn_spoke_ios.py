#Log into routers via loop

#Allows login via ssh
from netmiko import ConnectHandler
import getpass
from datetime import datetime

#Prompt the user for a password upon login.
my_pass = getpass.getpass()

#Get date and time.
now = datetime.now()
current_time = now.strftime("%Y-%m-%d")

#Create a file name called 'next_gen_asn.txt' and open the file.
asn_file = 'spoke_ios_asn.txt'
log_file = open(asn_file, "a")

#Log into each router. IP list of routers is stored in the ng_nxos_devices.txt file.

with open('spoke_ios_devices_mod.txt') as routers:
    for IP in routers:
        router = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': '206472656',
        'password': my_pass,
        'port': 22
        }

        net_connect = ConnectHandler(**router)

        
        #Backup device config.

        hostname = net_connect.send_command('sh run | inc hostname')
        hostname_split = hostname.split()
        hostname_mod = hostname_split[1]

        print('Backing up ' + hostname_mod + '-' + str(current_time) + '.txt')
        filename = 'backup2/' + hostname_mod + '-' + str(current_time) + '.txt'
        
        show_run = net_connect.send_command('show run')

        backup_file = open(filename, "a")
        backup_file.write(show_run)
        
        #Get router BGP ASN, save it to a variable.

        show_bgp = net_connect.send_command('show run | inc router bgp')
        #print(len(show_bgp))
        
        if (len(show_bgp) != 0):
            asn_split = show_bgp.split()
            asn_mod = asn_split[2]
            asn_list = hostname_mod + ',' + asn_mod
            print(asn_list)
            print('\n')
        else :
            asn_list = hostname_mod + ',no bgp'
            print(asn_list)

        #Add the value of the asn_list variable to the log_file file.
        log_file.write(asn_list)
        log_file.write('\n')
        
        net_connect.disconnect

backup_file.close()
log_file.close()

