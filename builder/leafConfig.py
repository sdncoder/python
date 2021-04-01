class interface(object):
    def __init__(self, vlan, ip, mask, vrf):
        self.vlan = vlan
        self.ip = ip
        self.mask = mask
        self.vrf = vrf
