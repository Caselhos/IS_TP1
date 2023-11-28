import psycopg2
from lxml import etree

# Query using XPath to retrieve album information by title

def listarAlbumTitulo(titulo):
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    host="localhost",
                                    port="5432",
                                    database="is")

        cursor = connection.cursor()

        cursor.execute(f"""
            SELECT xpath('//aura/Albums/Album[ALBUMINFO/@name="{titulo}"]', "imported_documents"."xml")
            FROM "imported_documents"
            WHERE "file_name" = 'spotify';
        """)

        result = cursor.fetchall()

        for row in result:
            album_name = row[0]
            print(f'Album Name: {album_name}')

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

