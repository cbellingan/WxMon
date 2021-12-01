import mysql
from utils import Config

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
