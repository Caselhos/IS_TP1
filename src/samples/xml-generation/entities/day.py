import xml.etree.ElementTree as ET


class Day:

    def __init__(self, date):
        Day.counter += 1
        self._id = date
        self._country = []
        self._music = []
        self._rank = []

    def add_country(self, country):
        self._country.append(country)

    def add_music(self, music):
        self._music.append(music)

    def add_rank(self, rank):
        self._rank.append(rank)

    def to_xml(self):
        el = ET.Element("Days")
        el.set("date", str(self._id))
        for index in self._country:
            item_element = ET.Element("countries")
            item_element.set("country_ref", str(index))
            for music, rank in zip(self._music, self._rank):
                day_el = ET.SubElement(item_element,"Songs")
                day_el.set("music_ref", str(music))
                day_el.set("rank", rank)
                item_element.append(day_el)
            el.append(item_element)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._id} ({self._id})"


Day.counter = 0
