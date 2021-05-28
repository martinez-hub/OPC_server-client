from opcua import Client
from time import sleep


#url and port to connect
client = Client("opc.tcp://127.0.0.1:4848")

#connecting to server
client.connect()
print("Client connected")

#printing server name
arr = client.get_namespace_array()
print(arr)


#temperature object node
Temp = client.get_objects_node()
print("The object node ID is: ", Temp)

#bring childrens (including value)
tempp = Temp.get_children()[1]
print("the name space and ID of variable object is: ", tempp)

#alternative to get node
state = client.get_node("ns=2;i=2")

#getting data from server and printing it
try:

    while 1:
        # printing temperature value
        for i in tempp.get_children():
            printing = i.get_value()
            print("The temperature is: ", printing)
            sleep(1)

except KeyboardInterrupt:
    client.close_session()
