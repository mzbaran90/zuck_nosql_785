import json


'''this class takes a record and returns a formatted json document
A record consists of node element objects and arrays. node elements will be accessed by calling <node>.text'''

class JSON(object):

    def __init__(self, record):
        self.record = record
        self.record_id = record.record_id.text
        self.title = record.title.text
        self.category = record.category.text
        self.date = record.date.text
        self.url = record.url.text

    def build_json_doc(self):
        unOfficJSON = {'record_id': self.record_id, 'title': self.title, 'speakers': self.record.speakers,
                       'category': self.category, 'date': self.date, 'url': self.url,
                       'statements': self.record.statements}

        officJSON = json.dumps(unOfficJSON, indent= 4)

        
        return officJSON
