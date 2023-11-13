import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader
from entities.country import Country
from entities.team import Team
from entities.player import Player
from entities.artist import Artist
from entities.album import Album
from entities.music import Music


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="country",
            builder=lambda row: Country(row["country"])
        )
        # read artists
        artists = self._reader.read_entities(
            attr="artists",
            builder=lambda row: Artist(row["artists"])
        )
        # read albums
        albums = self._reader.read_entities(
            attr="album_name",
            builder=lambda row: Album(
                name=row["album_name"],
                release_date=row["album_release_date"]
            )
        )
        # read musics
        #TODO resolver isto porque nao esta a chamar a referencia ao pais mas sim a sigla
        musics =self._reader.read_entities(
            attr="name",
            builder=lambda row: Music(
                spotify_id=row["spotify_id"],
                name=row["name"],
                rank=row["daily_rank"],
                country=countries[row["country"]],
                artist=artists[row["artists"]],
                album=albums[row["album_name"]]
            )
        )
        # read players
        """
        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["Current Club"]].add_player(player)

        self._reader.read_entities(
            attr="full_name",
            builder=lambda row: Player(
                name=row["full_name"],
                age=row["age"],
                country=countries[row["nationality"]]
            ),
            after_create=after_creating_player
        )
        """
        # generate the final xml
        root_el = ET.Element("Football")

        teams_el = ET.Element("Teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

