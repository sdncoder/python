# create SVI interfaces
class intVlan(object):
    def __init__(self, vlan, ip, mask, vrf):
        self.vlan = vlan
        self.ip = ip
        self.mask = mask
        self.vrf = vrf

# create bogon ACL on interface facing interfaces
class bogon(object):
    def __init__(self, srcip, srcsub, dstip, dstsub, state):
        self.srcip = srcip
        self.srcsub = srcsub
        self.dstip = dstip
        self.dstsub = dstsub
        self.state = state
