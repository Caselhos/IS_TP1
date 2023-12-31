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
    print("4. Query 1 PLACEHOLDER")
    print("5. Query 2 Listar Album por Titulo")
    print("6. Query 3 Listar ALbum por Data")
    print("7. Query 4 Listar Musicas por Artista")
    print("8. Query 5 PLACEHOLDER")
    print("9. Exit")


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
        print(f" > {server.listarTitulo()}")

    elif choice == '5':
        titulo = input("Enter the album title: ")
        filename = input("Enter the name of the file: ")
        print(f" > {server.listarAlbumTitulo(titulo,filename)}")

    elif choice == '6':
        data = input("Enter the date: ")
        filename = input("Enter the name of the file: ")
        print(f" > {server.listarAlbumData(data,filename)}")

    elif choice == '7':
        artista = input("Enter the artist title: ")
        filename = input("Enter the name of the file: ")
        print(f" > {server.listarMusicaArtista(artista,filename)}")

    elif choice == '8':
        print(f" > {server.listarPLACEHOLDER()}")

    elif choice == '9':
        print("Exiting program. Goodbye!")
        break


    else:
        print("Invalid choice. Please enter a number between 1 and 5.")