

# List already containing all ip/mask (format: 10.10.10.0/255.255.255.0') shown above
print ip_mask_list
#hardcoded mask for testing
netmask = "255.255.248.0"
#convert mask to CIDR
cidr = sum([bin(int(x)).count('1') for x in netmask.split('.')])
print cidr  # prints 21

