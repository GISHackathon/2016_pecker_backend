import pydocumentdb.document_client as document_client
from pecker import config
from pydocumentdb.errors import HTTPFailure


class ErrorDbHandler(object):
    doc_client = document_client.DocumentClient(
        config.DB_HOST,
        {'masterKey': config.DB_KEY}
    )
    error_coll_link = config.DB_DATABASE_LINK+config.DB_COLLECTION_LINK

    @classmethod
    def import_tweet(cls, tweet_id, user_id, text, x_coord, y_coord, created_at, tweet_type, img_url):
        try:
            cls.doc_client.CreateDocument(
                cls.error_coll_link,
                {
                    'id': tweet_id,
                    'user_id': user_id,
                    'text': text,
                    'x_coord': x_coord,
                    'y_coord': y_coord,
                    'created_at': created_at,
                    'type': tweet_type,
                    'img_url': img_url
                }
            )
        except HTTPFailure as e:
            if e.status_code != 409:
                raise e
            else:
                print 'Already in DB...'

    @classmethod
    def get_all_errors(cls):
        errs = cls.doc_client.ReadDocuments(cls.error_coll_link)
        return list(errs)

