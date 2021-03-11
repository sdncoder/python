
I have a list containing hundreds of ip addresses and masks in this format:

['10.10.10.0/255.255.255.0', '10.10.20.0/255.255.255.192']
I would like to convert this list to this format:

['10.10.10.0/24', '10.10.20.0/26']
Here is my code:

# List already containing all ip/mask (format: 10.10.10.0/255.255.255.0') shown above
print ip_mask_list
#hardcoded mask for testing
netmask = "255.255.248.0"
#convert mask to CIDR
cidr = sum([bin(int(x)).count('1') for x in netmask.split('.')])
print cidr  # prints 21

