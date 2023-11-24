import xml.etree.ElementTree as ET
from .artist import Artist

class Music:

    def __init__(self, spotify_id, name, rank, country, album):
        Music.counter += 1
        self._id = Music.counter
        self._spotify_id = spotify_id
        self._name = name
        #self._rank = rank
        #self._country = country
        self._artists = []
        self._album = album

    def to_xml(self):
        el = ET.Element("Music")
        el.set("id", str(self._id))
        el.set("spotify_id", str(self._spotify_id))
        el.set("album_ref", str(self._album.get_id()))
        test = ET.SubElement(el, "MUSICINFO")
        test.set("name", self._name)
        #el.set("name", self._name)
        #el.set("rank", self._rank)
        #el.set("country_ref", str(self._country.get_id()))
        players_el = ET.SubElement(el, "Artists")
        for player in self._artists:
            players_el.append(player.to_xml())
        #el.set("artist_ref", str(self._artist.get_id()))


        return el

    def add_player(self, artist: Artist):
        self._artists.append(artist)
    def get_id(self):
        return self._id
    """
    def get_rank(self):
        return self._rank

    def get_country(self):
        return self._country
    """
    def __str__(self):
        return (f"{self._name}, spotify_id:{self._spotify_id}, rank:{self._rank}, country:{self._country}, "
                f"artist:{self._artist}, album:{self._album}")


Music.counter = 0
