#import sw_vars variable file  as Python module
import sw_vars

# readin the switch template text file
from string import Template
filein = open( 'switch_template.txt' )
src = Template( filein.read())


# ordered list of varialbes to be substituted into template $ variables from sw_vars
#
d={ 'hostname':sw_vars.hostname,
'loopback1':sw_vars.loopback1,
'loopback2':sw_vars.loopback2,
'loopback3':sw_vars.loopback3,
'loopback4':sw_vars.loopback4,
'loopback5':sw_vars.loopback5,
'loopback6':sw_vars.loopback6,
'vlan10':sw_vars.vlan10
}

# output file
result = src.substitute(d)
print result
