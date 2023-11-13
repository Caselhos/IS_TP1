import xml.etree.ElementTree as ET


class Album:

    def __init__(self, name, release_date):
        Album.counter += 1
        self._id = Album.counter
        self._name = name
        self._release_date = release_date

    def to_xml(self):
        el = ET.Element("Album")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("release_date",self._release_date)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, release_date:{self._release_date}"


Album.counter = 0
