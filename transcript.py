import json

class Transcript(object):
    """
    Extracts and stores information about a single transcript in the Zuckerber Files.
    """
    def __init__(self, tree):
        self.record_id = tree.find('./metadata/record_id')
        self.title = tree.find('./metadata/title')
        self.category = tree.find('./metadata/type')
        self.date = tree.find('./metadata/date')
        self.url = tree.find('./metadata/url')
        self.statements = []
        for i, statement in enumerate(tree.findall('./contents/participant')):
            statement = {
                'speaker': statement.attrib.get('name'),
                'statement': statement.text,
                'position': i
            }
            self.statements.append(statement)

    def __repr__(self):
        return json.loads(to_dict(self))


def to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """

    #  Populate the dictionary with object meta data
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict



