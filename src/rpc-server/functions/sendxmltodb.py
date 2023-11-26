import xml.etree.ElementTree as ET
import psycopg2


def xmltodb(xml_data,name):
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                      password="is",
                                      host="is-db",
                                      port="5432",
                                      database="is")

        #teste = etree.parse(xml_data.data)

        with connection.cursor() as cursor:
            """""
            with open(path, 'r', encoding="utf8") as file:
                xml_data = file.read()
            """""

            root = ET.fromstring(xml_data.data)
            #print(xml_data)
            #print(teste)
            #print(root)
            cursor.execute(
                "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)",
                (name, xml_data.data.decode())
            )

            connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)
        return "Failed"

    finally:
        if connection:
            connection.close()

    return "Sucess"


