import psycopg2

# Query using XPath to retrieve music information by artist name

def listarAlbumData(date):
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

        # Use XPath in the SQL query to extract music information by artist name
        sql_query = f"""
            SELECT xpath('//aura/Albums/Album[ALBUMINFO/@release_date="{date}"]', "imported_documents"."xml")
            FROM "imported_documents"
            WHERE "file_name" = 'spotify';
            """
        #se mudar o '=' para '<' ou '>' não printa direito

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        for row in rows:
            result = row[0]
            
            print("Album Info:", result)

    finally:
        if connection:
            cursor.close()
            connection.close()

#listarAlbumData("2022-09-23")
