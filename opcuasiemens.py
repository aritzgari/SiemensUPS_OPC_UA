#Aunque no este importada hay que instalar cryptography: pip install cryptography
#pip install opcua para instalar la librería de 
from opcua import Client

# Replace these with your server URL, username, and password
endpoint_url = "opc.tcp://192.168.4.11:4840"
username = "admin"
password = "!Casta32"
# Replace these with your node ID
node_battery_voltage = "ns=3;i=100215"
node_output_current = "ns=3;i=100222"
node_output_voltage = "ns=3;i=100203"
node_battery_charge = "ns=3;i=100191" #porcentaje de bateria
# Create a client instance
client = Client(endpoint_url)
client.session_timeout = 360000  # Timeout in milliseconds
try:
    # Set user credentials
    client.set_user(username)
    client.set_password(password)
    # Connect to the server
    client.connect()
    #print("Connected to OPC UA server")
    # Get the node to read
    node = client.get_node(node_output_current)
    # Read the value of the node
    value = node.get_value()
    print(f"Value of node {node_output_current}: {value}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    try:
        # Disconnect from the server if connected
        client.disconnect()
        #print("Disconnected from OPC UA server")
    except Exception as e:
        print(f"An error occurred while disconnecting: {e}")