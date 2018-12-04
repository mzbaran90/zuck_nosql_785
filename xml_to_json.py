import os
from xml.etree import ElementTree as ET
import glob
import Record




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


if __name__ == '__main__':
    set_working_directory()
    filenames = get_filenames()
    for file in filenames:
        tree = create_xml_tree(file)
        record = Record.Record(tree)
        print(record.statements)

















