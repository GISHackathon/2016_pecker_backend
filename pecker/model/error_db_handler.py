import pydocumentdb.document_client as document_client
from pecker import config
from pydocumentdb.errors import HTTPFailure


class ErrorDbHandler(object):
    doc_client = document_client.DocumentClient(
        config.DB_HOST,
        {'masterKey': config.DB_KEY}
    )
    error_coll_link = config.DB_DATABASE_LINK + config.DB_ERRORS_COLLECTION_LINK

    @classmethod
    def import_error(cls, kat_id, x_coord, y_coord):
        try:
            cls.doc_client.CreateDocument(
                cls.error_coll_link,
                {
                    'kat_id': kat_id,
                    'x_coord': x_coord,
                    'y_coord': y_coord
                }
            )
        except HTTPFailure as e:
            if e.status_code != 409:
                raise e
            else:
                print 'Already in DB...'

    @classmethod
    def get_all_errors(cls):
        print cls.error_coll_link
        errs = cls.doc_client.ReadDocuments(cls.error_coll_link)

        return list(errs)
