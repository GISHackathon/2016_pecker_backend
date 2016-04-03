import pydocumentdb.document_client as document_client
from pecker import config
from pydocumentdb.errors import HTTPFailure

class UserDbHandler(object):
    doc_client = document_client.DocumentClient(
        config.DB_HOST,
        {'masterKey': config.DB_KEY}
    )
    user_coll_link = config.DB_DATABASE_LINK + config.DB_USERS_LINK

    @classmethod
    def create_user(cls, data):
        try:
            cls.doc_client.CreateDocument(
                cls.user_coll_link,
                {
                    "username": data["screen_name"],
                    "name": data["name"]
                }
            )
        except HTTPFailure as e:
            if e.status_code != 409:
                raise e
            else:
                print 'Already in DB...'

    @classmethod
    def get_user(cls, username):
        # TODO
        pass
