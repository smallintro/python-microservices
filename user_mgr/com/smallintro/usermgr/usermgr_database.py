from logzero import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBInit:

    def __init__(self):
        _db_connect_str = 'postgres://postgres:ABC_abc1@localhost:5432/postgres'
        try:
            logger.debug(_db_connect_str)
            self.engine = create_engine(_db_connect_str,echo=True)
            self.connection = None # TODO

            Session = sessionmaker(bind=self.engine)
            self.session = Session()

            Base.metadata.create_all(self.engine)
        except Exception as e:
            logger.exception(f"DB init failed ",e)


    def get_connection(self):
        return self.connectin

    def get_session(self):
        return self.session

gconnection = None
gsession = None
def get_db_connection():
    global gconnection
    if gconnection is None:
        gconnection = DBInit().get_connection()
    return gconnection

def get_db_session():
    global gsession
    if gsession is None:
        gsession = DBInit().get_session()
    return gsession

