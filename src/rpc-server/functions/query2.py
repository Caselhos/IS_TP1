import psycopg2
from lxml import etree

# Query using XPath to retrieve album information by title

def listarAlbumTitulo(titulo,filename):
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    host="is-db",
                                    port="5432",
                                    database="is")

        cursor = connection.cursor()
        cursor.execute("""
            SELECT xpath('//aura/Albums/Album/ALBUMINFO[@name= "%s"]',"imported_documents"."xml")
            FROM "imported_documents"
            WHERE file_name = '%s';
        """, (titulo, filename))

        result = cursor.fetchall()

        for row in result:
            albumInfo = row[0]
            print("Album Info: ", albumInfo)
        return result
    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)
        return error

    finally:
        if connection:
            cursor.close()
            connection.close()

