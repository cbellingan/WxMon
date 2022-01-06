import dao
import mysql.connector


class DB(dao.DbBase):
    def __init__(self, config):
        self._password = config.password
        self._username = config.username
        self._db_endpoint = config.endpoint
        self._db_port = config.port
        self._db_name = config.db
        self._connection = None
    
    def connection(self):
        if self._connection is None:
            self._connection = mysql.connector.connect(
                user=self._username, 
                database=self._db_name, 
                host=self._db_endpoint, 
                password=self._password, 
                port=self._db_port
            )
        return self._connection

    def cursor(self):
        return self.connection().cursor()
    
    def execute(self, sql_string):
        cur = self.cursor()
        cur.execute(sql_string)
        return cur.fetchall()
