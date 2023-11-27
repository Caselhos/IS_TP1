import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.album import Album
from entities.artist import Artist
from entities.country import Country
from entities.day import Day
from entities.music import Music

#todo fazer com que cada artista seja uma entry no programa
class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):


        # read days
        days = self._reader.read_entities(
            get_keys=lambda row: row["snapshot_date"],
            builder=lambda row: Day(
                date=row["snapshot_date"],
            )
        )

        # read albums
        albums = self._reader.read_entities(
            get_keys=lambda row: row["album_name"],
            builder=lambda row: Album(
                name=row["album_name"],
                release_date=row["album_release_date"]
            )
        )

        def after_creating_country(rcountry, row):
            for x in days.values():
                x.add_country((rcountry.get_id()))
        #read countries
        countries = self._reader.read_entities(
            get_keys=lambda row: row["country"],
            builder=lambda row: Country(row["country"])
            , after_create=after_creating_country
        )

        # read musics
        musics = self._reader.read_entities(
            get_keys=lambda row: row["name"],
            builder=lambda row: Music(
                spotify_id=row["spotify_id"],
                name=row["name"],
                rank=row["daily_rank"],
                country=countries[row["country"]],
                album=albums[row["album_name"]]
            )
        )

        def after_creating_artist(artist,row):
            musics[row["name"]].add_player(artist)
        # read artists
        artists = self._reader.read_entities(
            get_keys=lambda row: row["artists"].replace(' ', '').split(","),
            builder=lambda row: Artist(row["artists"])
            , after_create=after_creating_artist

        )
        """
        for x in days.values():
            x.add_data(musics)
        """
        def after_creating_music(music, row):
            days[row["snapshot_date"]].add_music(music.get_id())
            days[row["snapshot_date"]].add_rank(music.get_rank())
            music[row["artists"]].add_artists(music)
            return

        # generate the final xml
        root_el = ET.Element("aura")

        musics_el = ET.Element("Musics")
        for music in musics.values():
            musics_el.append(music.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        artists_el = ET.Element("Artists")
        for artist in artists.values():
            artists_el.append(artist.to_xml())

        albums_el = ET.Element("Albums")
        for album in albums.values():
            albums_el.append(album.to_xml())

        days_el = ET.Element("Days")
        for day1 in days.values():
            days_el.append(day1.to_xml())

        #root_el.append(days_el) NAO APAGAR
        root_el.append(musics_el)
        root_el.append(artists_el)
        root_el.append(albums_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        path = "./createdxml.xml"
        with open(path, "w") as writer:
            writer.write(dom.toprettyxml())
        return dom.toprettyxml()
