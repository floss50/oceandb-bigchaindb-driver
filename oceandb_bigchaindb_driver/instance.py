from bigchaindb_driver import BigchainDB

_DB_INSTANCE = None


def get_database_instance(config_file=None):
    global _DB_INSTANCE
    if _DB_INSTANCE is None:
        _DB_INSTANCE = BigchainDBInstance(config_file)

    return _DB_INSTANCE


class BigchainDBInstance(object):

    def __init__(self, config):
        host = config['db.hostname']
        port = int(config['db.port'])
        app_id = config['db.app_id']
        app_key = config['db.app_key']
        bdb_root_url = '%s:%s' % (host, port)
        # bdb_root_url = 'https://%s:%s' % (host, port)
        tokens = {'app_id': app_id, 'app_key': app_key}

        self._bdb = BigchainDB(bdb_root_url, headers=tokens)



    @property
    def instance(self):
        return self._bdb

