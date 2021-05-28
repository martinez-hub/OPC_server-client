from time import sleep
import random
from opcua import Server, ua, uamethod


#OPC UA server set up

if __name__ == "__main__":

    #server function
    server = Server()

    #url and port
    endpoint = "opc.tcp://127.0.0.1:4848"
    server.set_endpoint(endpoint)

    #setting server name
    servername = "Python-OPC-UA-Server"
    server.set_server_name(servername)


    #object node and variable node modeling
    #opc ua modeling
    root_node = server.get_root_node() #root node
    object_node=server.get_objects_node() #variable to create objects
    id = server.register_namespace("OPCUA_SERVER") #id

    #creating object per variable
    myobj = object_node.add_object(id,"Variables") #test object
    turbine = object_node.add_object(id,"Turbine") #state variable to write

    #printing objects information
    print("Root Node ID: ", root_node)
    print("Object Node ID: ", object_node)
    print("Name space and ID of Variable Object: ", myobj)
    print("Name space and ID of Turbine Object: ", turbine)

    #add variable in test object
    Temp = myobj.add_variable(id, "Temperature", 0,ua.VariantType.Float)

    #add variable in turbine object
    turb = turbine.add_variable(id, "Turbine", 0, ua.VariantType.Float)

    #setting writable the variable
    turb.set_writable(True)

    #printing variable information
    print("Name Space and ID of Temperature: ", Temp)

    #starting server
    print("Server started at{}".format(endpoint))
    server.start()

    try:

        #loop for update variables
        while 1:


            #setting value on temperature variable
            Temp.set_value(random.randint(100,110), ua.VariantType.Float)

            #sleep one second
            sleep(1)



    except KeyboardInterrupt:
        server.stop()






