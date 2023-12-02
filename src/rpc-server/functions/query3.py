import psycopg2

# Query using XPath to retrieve music information by artist name

def listarAlbumData(date,filename):
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

        # Use XPath in the SQL query to extract music information by artist name
        sql_query = """
            SELECT xpath('//aura/Albums/Album[ALBUMINFO/@release_date= %s]', "imported_documents"."xml")
            FROM "imported_documents"
            WHERE "file_name" = '%s';
            """
        #se mudar o '=' para '<' ou '>' não printa direito

        cursor.execute(sql_query, (date, filename, ))

        rows = cursor.fetchall()

        for row in rows:
            result = row[0]
            
            print("Album Info:", result)
        return rows
    finally:
        if connection:
            cursor.close()
            connection.close()

#listarAlbumData("2022-09-23")
