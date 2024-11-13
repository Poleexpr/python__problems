import json
import xmltodict

with open("cards.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

    json_data = json.dumps(data_dict, ensure_ascii=False)

    with open("cards.json", "w") as json_file:
        json_file.write(json_data)