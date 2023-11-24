import xml.etree.ElementTree as ET


class Day:

    def __init__(self, date):
        Day.counter += 1
        self._id = date
        self._country = []
        self._music = []
        self._rank = []
        self._data = {}
        #data = {datetime.datetime.strptime(date, "%Y-%m-%d"): (1, 2) for date in dates}
    def add_country(self, country):
        self._country.append(country)
        self._data[country] = []

    def add_data(self, musics):
        arroz = []
        for y in self._data.keys():
            for x in musics.values():
                if x.get_id() in arroz:
                    continue
                #arroz.append(x.get_id())
                else:
                    arroz.append(x.get_id())
                    #arroz.append(x.get_id())
                    #self._data.update({y: x.get_id()})
            self._data.update({y:arroz})
            arroz.clear()

    def add_music(self, music):
        self._music.append(music)

    def add_rank(self, rank):
        self._rank.append(rank)

    def to_xml(self):
        el = ET.Element("Day")
        el.set("date", str(self._id))
        for index in self._country:
            item_element = ET.Element("countries")
            item_element.set("country_ref", str(index))
            """
            for music, rank in zip(self._music, self._rank):
                day_el = ET.SubElement(item_element, "Songs")
                day_el.set("music_ref", str(music))
                day_el.set("rank", rank)
                item_element.append(day_el)
            """
            for x in self._data.values():
                day_el = ET.SubElement(item_element, "Songs")
                day_el.set("music_ref", str(x))
            el.append(item_element)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"{self._id} ({self._id})"


Day.counter = 0
