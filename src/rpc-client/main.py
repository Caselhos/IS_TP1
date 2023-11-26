import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')
path = "dsa.xml"  # input do cliente
path_schema = "dsa.xsd"  # input do cliente

with open(path, 'rb') as file:
    xml_data = xmlrpc.client.Binary(file.read())
with open(path_schema, 'rb') as file:
    xml_schema = xmlrpc.client.Binary(file.read())


name = "fd2sfds"  # input do cliente
print(f" > {server.xmltodb(xml_data, name)}")

print(f" > {server.validate_xml_with_schema(xml_data,xml_schema)}")

filetobedeleted="fdsfds"  # input do cliente
print(f" > {server.softdelete(filetobedeleted)}")
