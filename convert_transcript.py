from glob import iglob
import json
from helpers import parse_xml, set_working_directory


class Transcript:
    """
    Extracts and stores information about a single transcript in the Zuckerberg Files.
    """
    def __init__(self, tree):
        self.record_id = get_text(tree, './metadata/record_id')
        self.title = get_text(tree, './metadata/title')
        self.category = get_text(tree, './metadata/type')
        self.date = get_text(tree, './metadata/date')
        self.url = get_text(tree, './metadata/url')
        self.statements = []
        for i, statement in enumerate(tree.findall('./contents/participant')):
            statement = {
                'speaker': statement.attrib.get('name'),
                'statement': statement.text,
                'position': i
            }
            self.statements.append(statement)


def get_text(tree, path):
    element = tree.find(path)
    if element is None:
        return None
    else:
        return element.text


if __name__ == '__main__':
    set_working_directory()
    for file in iglob('XML/*.xml'):
        tree = parse_xml(file)
        transcript = Transcript(tree)
        with open('JSON/{}.txt'.format(transcript.record_id), 'w') as outfile:
            json.dump(transcript.__dict__, outfile)


















