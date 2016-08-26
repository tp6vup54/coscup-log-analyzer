import redis

class Dao():
    def __init__(self, db_url='127.0.0.1:6379'):
        self.conn_pool = redis.ConnectionPool.from_url(url=db_url)
        self.test_connection()

    def test_connection(self):
        r = self.__get_conn()
        r.ping()

    def __get_conn(self):
        return redis.Redis(connection_pool=self.conn_pool)