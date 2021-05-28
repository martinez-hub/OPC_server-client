import OpenOPC
import pywintypes #to avoid timeout error
import time

pywintypes.datetime = pywintypes.TimeType

# if you have MAC use this connection
# opc = OpenOPC.open_client('localhost')

# if you have windows use this one
opc = OpenOPC.client()

# verifying servers
servers = opc.servers()
print(servers)

# connecting to server
opc.connect('Matrikon.OPC.Simulation.1')

#listing available aliases
aliases = opc.list()
print (aliases)

#listing available groups in specific alias
groups = opc.list('Simulation Items')
print(groups)

#available tags in specific group
tags = opc.list('Simulation Items.Random.*')
print(tags)

#reading Tag values
reading = opc.read('Random.ArrayOfReal8')
print(reading)

opc.close()
