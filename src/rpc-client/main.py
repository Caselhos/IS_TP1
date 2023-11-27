import xmlrpc.client


def connect_to_server():
    print("Connecting to server...")
    return xmlrpc.client.ServerProxy('http://is-rpc-server:9000')


def read_file(file_path):
    with open(file_path, 'rb') as file:
        return xmlrpc.client.Binary(file.read())


def main_menu():
    print("1. XML to Database")
    print("2. Validate XML with Schema")
    print("3. Soft Delete File")
    print("4. Exit")


server = connect_to_server()

while True:
    main_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        path = input("Enter XML file path: ")
        name = input("Enter a name: ")
        xml_data = read_file(path)
        print(f" > {server.xmltodb(xml_data, name)}")

    elif choice == '2':
        xml_path = input("Enter XML file path: ")
        schema_path = input("Enter XML schema file path: ")
        xml_data = read_file(xml_path)
        xml_schema = read_file(schema_path)
        print(f" > {server.validate_xml_with_schema(xml_data, xml_schema)}")
        print("****** '> None' Significa sem problemas *******")

    elif choice == '3':
        file_to_delete = input("Enter the file to soft delete: ")
        print(f" > {server.softdelete(file_to_delete)}")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")