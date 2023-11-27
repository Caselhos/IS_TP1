import psycopg2
from lxml import etree

# Query using XPath to retrieve music information by artist name

def listarMusicasPorArtista(artist_name):
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
        cursor.execute(f"""
            SELECT "imported_documents"."xml"
            FROM "imported_documents"
            WHERE "file_name" = 'spotify'
            AND xpath_exists('//aura/Musics/Music[Artists/Artist[@name="{artist_name}"]]', "imported_documents"."xml");
        """)

        result = cursor.fetchall()

        for row in result:
            music_xml = row[0]

            if music_xml:
                # Parse the XML and print music information
                music_root = etree.fromstring(music_xml)
                music_name = music_root.xpath('//Music/MUSICINFO/@name')[0]
                artist_name = music_root.xpath('//Music/Artists/Artist/@name')[0]

                print(f'Artist: {artist_name}, Music: {music_name}')
        else:
            print(f'No music found for artist: {artist_name}')

    except (Exception, psycopg2.Error) as error:
        print("Failed to fetch data", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

listarMusicasPorArtista("Dionela")
