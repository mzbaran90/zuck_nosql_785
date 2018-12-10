from glob import iglob
from json import load
from pymongo import MongoClient, ASCENDING, DESCENDING
from helpers import set_working_directory


if __name__ == '__main__':

    # Authentication
    client = MongoClient('localhost', 27017)
    db = client.zuck

    # Indexing
    db.transcripts.create_index(['record_id', DESCENDING], unique=True)
    db.transcripts.create_index(['title', ASCENDING])
    db.transcripts.create_index(['date', DESCENDING])
    db.transcripts.create_index(['source', ASCENDING])
    db.transcripts.create_index(['type', ASCENDING])
    db.transcripts.create_index(['format', ASCENDING])
    db.transcripts.create_index(['statements.speaker', ASCENDING])
    db.transcripts.create_index(['url', ASCENDING])
    db.transcripts.create_index({
        'title': 'text',
        'description': 'text',
        'statements.statement': 'text'
    })
    db.transcripts.create_index({
        'statements.speaker': ASCENDING,
        'statements.position': ASCENDING
    })
    db.transcripts.create_index({
        'statements.speaker': ASCENDING,
        'date': DESCENDING
    })
    db.transcripts.create_index({
        'statements.speaker': ASCENDING,
        'format': ASCENDING
    })
    db.transcripts.create_index({
        'statements.speaker': ASCENDING,
        'source': ASCENDING
    })

    # Insert transcript documents
    set_working_directory()
    for file in iglob('JSON/*.txt'):
        with open(file, 'r') as handle:
            json = load(handle)
            result = db.transcripts.insert_one(json)