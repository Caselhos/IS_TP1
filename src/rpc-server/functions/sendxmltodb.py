import psycopg2
from lxml import etree

conn = psycopg2.connect(
    host='your_host',
    database='your_database',
    user='your_username',
    password='your_password'
)

with conn.cursor() as cursor:
    for row in parser.findall('your_xml_element'):
        # Map the XML elements to the corresponding table columns
        file_name = row.find('your_file_name_element').text
        xml_data = etree.tostring(row.find('your_xml_data_element'))

        # Insert the data into the table
        cursor.execute(
            "INSERT INTO public.imported_documents (file_name, xml) VALUES (%s, %s)",
            (file_name, xml_data)
        )

    conn.commit()

conn.close()