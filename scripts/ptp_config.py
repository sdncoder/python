#Allows login via ssh
from netmiko import ConnectHandler
import getpass

#Prompt the user for a password upon login.
my_pass = getpass.getpass()

#Log into each leaf/spine switch. IP list of switches is stored in the lab_ipfm_devices.txt file.

with open("lab_ipfm_devices.txt") as switches:
    for IP in switches:
        switch = {
        'device_type': 'cisco_nxos',
        'ip': IP,
        'username': 'username',
        'password': my_pass,
        }

        net_connect = ConnectHandler(**switch)

        
        #Count the number of interfaces on each switch and print it out. Set the number equal to a variable.
        
        print('Connecting to ' + IP)
        output = net_connect.send_command('sh int status')
        interface_count = output.count("Eth")
        #print(interface_count)
       
        #Back up the config for each switch

        hostname = net_connect.send_command('sh hostname')
        hostname_mod = hostname.strip()
        print('Backing up ' + hostname_mod + '.txt')
        filename = 'backup2/' + hostname_mod + '.txt'
        show_run = net_connect.send_command('show run')
        show_vlan = net_connect.send_command('show vlan')
        show_version = net_connect.send_command('show ver')
        log_file = open(filename, "a")
        log_file.write(show_run)

        #Add PTP commands to each interface.  

        config_commands = ['int Eth1/1-' + str(interface_count),
                           'ptp',
                           'ptp announce interval 0']
        output2 = net_connect.send_config_set(config_commands)  

        #Save the configuration

        output2 += net_connect.save_config()

        #Print the changes made.

        print(output2)
           
        #Verification. Save a copy of the new config and verify changes were applied correctly.
 
        print("Backing up " + hostname_mod + '-new.txt')
        filename = 'backup2/' + hostname_mod + '-new.txt'
        show_start = net_connect.send_command('show start')
        show_vlan = net_connect.send_command('show vlan')
        log_file = open(filename, "a")
        log_file.write(show_start)
        print('\n')
            
        net_connect.disconnect
