import psycopg2

# Query using XPath to retrieve music information by artist name

def listarMusicaArtista(artist,filename):
    global cursor
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(user="is",
                                    password="is",
                                    post="is-db",
                                    port="5432",
                                    database="is")

        cursor = connection.cursor()

        # Use XPath in the SQL query to extract music information by artist name
        sql_query = f"""
            SELECT xpath('//aura/Musics/Music[Artists/Artist/@name="{artist}"]', "imported_documents"."xml")
            FROM "imported_documents"
            WHERE "file_name" = {filename};
            """

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        for row in rows:
            result = row[0]
            
            print("Musicas do artista: ", result)
        return rows
    finally:
        if connection:
            cursor.close()
            connection.close()

#listarMusicaArtista("Ariana Grande")
