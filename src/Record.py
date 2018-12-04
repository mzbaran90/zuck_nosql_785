from xml.etree import ElementTree as ET

class Record():

    def __init__(self, tree):
        '''
        :param tree:
        instance variables are assigned from attrs in xml tree object. arrays are set in respective methods.
        Type will now be category.
        Use node.text to extract text for attributes.
        '''

        self.tree = tree
        self.record_id = tree.find('./metadata/record_id')
        self.title = tree.find('./metadata/title')
        self.category = tree.find('./metadata/type')
        self.date = tree.find('./metadata/date')
        self.url = tree.find('./metadata/url')
        self.speakers = self.setSpeakers()
        self.statements = self.setStatements()



    def setSpeakers(self):
        '''
        participants are seperated as semi-colon in xml files there for a split is conducted so that each speaker
        will be it's own value. return participantSplitList.
        In JSON docs, participants will now be known as speakers

        '''
        participantsSingle = self.tree.find('./metadata/participants')
        participantSplit = participantsSingle.text.split(';')

        ## some funky formatting within participants. Quick check for space since a split on ';' was conducted

        #listParticipants = [participant.strip() for participant in participantSplit if not participant.isspace()]

        listParticipants = []
        for participant in participantSplit:
            if not participant.isspace() and participant != "":
                listParticipants.append(participant)

        return listParticipants

    def setStatements(self):
        '''
        :return listStatements:
        extract speakers and their corresponding text and append each statement into a list of statements.
        Each statement will be a dictionary containing {name : <speaker name>, text:<statement text>,
        pos: paragraph position}
        '''

        listStatements = []

        for pos, node in enumerate(self.tree.findall('./contents/participant')):
            statement = {'speaker': node.attrib.get('name'), 'statement': node.text, 'pos': pos}
            listStatements.append(statement)
        return listStatements


