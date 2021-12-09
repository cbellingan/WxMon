import dao

from utils import Config
# from dao import DbBase

class MySqlDBWriter(dao.DbBase):
    pass

def depr():
    #TODO define the interface here
    cfg = Config('MySqlDb')
    cnx = mysql.connector.connect(
        user=cfg.username, 
        database=cfg.db, 
        host=cfg.endpoint, 
        password=cfg.password, 
        port=cfg.port
    )
    cursor = cnx.cursor()
