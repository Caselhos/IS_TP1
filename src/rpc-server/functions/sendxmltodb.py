from lxml import etree
import xml.etree.ElementTree as ET
import psycopg2

connection = None
cursor = None
path = "dsa.xml"
try:
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")

    parser = etree.parse(path)

    with connection.cursor() as cursor:
        with open(path, 'r', encoding="utf8")as file:
            xml_data = file.read()
        root = ET.fromstring(xml_data)
        cursor.execute(
                "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)",
                (path, xml_data)
        )

        connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Failed to fetch data", error)

finally:
    if connection:
        connection.close()


