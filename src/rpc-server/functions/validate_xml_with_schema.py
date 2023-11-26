import xmlschema


def validate_xml_with_schema(xml_data, xml_schema):

    return xmlschema.validate(xml_data.data.decode(), xml_schema.data.decode())


