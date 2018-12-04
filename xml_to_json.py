import os
from xml.etree import ElementTree as ET
import glob
import Record
import JsonCreate

def set_working_directory():
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

def get_filenames():
    for filenames in glob.iglob('*.xml'):
        yield filenames

def create_xml_tree(file):
    with open(file, 'r', encoding='utf-8') as infile:
        tree = ET.parse(infile)
        return tree

def write_json_file(file, jsonDoc):
    with open(file + '.json', 'w', encoding='utf-8') as outfile:
        outfile.write(jsonDoc)


if __name__ == '__main__':
    set_working_directory()
    filenames = get_filenames()

    for file in filenames:
        tree = create_xml_tree(file)
        record = Record.Record(tree)
        json_instance = JsonCreate.JSON(record)
        jsonDoc = json_instance.build_json_doc()
        write_json_file(file.split('.')[0], jsonDoc)


















