import pydocumentdb.document_client as document_client
from pecker import config
from pydocumentdb.errors import HTTPFailure

class SessionDbHandler(object):
    doc_client = document_client.DocumentClient(
        config.DB_HOST,
        {'masterKey': config.DB_KEY}
    )
    session_coll_link = config.DB_DATABASE_LINK + config.DB_SESSIONS_LINK

    @classmethod
    def create_session(cls, session_id, key, value):
        try:
            cls.doc_client.CreateDocument(
                cls.session_coll_link,
                {
                    'session_id': session_id,
                    'key': key,
                    'value': value
                }
            )
        except HTTPFailure as e:
            if e.status_code != 409:
                raise e
            else:
                print 'Already in DB...'

    @classmethod
    def get_session(cls, session_id, key):
        print cls.session_coll_link
        sessions = cls.doc_client.ReadDocuments(cls.session_coll_link)

        for session in list(sessions):
            if session['session_id']==session_id and session['key']==key:
                return session['value']

        return ''
