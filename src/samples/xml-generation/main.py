from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/universal_top_spotify_songs.csv")
    print(converter.to_xml_str())
