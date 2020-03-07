from logzero import logger as log
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app_config import *

Base = declarative_base()

global_db_obj = None

db_connection = None

db_session = None


class DBInit:
    def __init__(self):
        log.info(f"__init__ BEGINS")
        try:
            self.engine = create_engine(db_connect_str, echo=True)
            self.connection = None  # TODO

            Session = sessionmaker(bind=self.engine)
            self.session = Session()

            Base.metadata.create_all(self.engine)
        except Exception as e:
            log.exception(f"DB init failed ", e)
        log.info(f"__init__ ENDS")

    def get_connection(self):
        return self.connectin

    def get_session(self):
        return self.session


class DataBaseObj:
    @staticmethod
    def init_db_obj():
        global global_db_obj
        if global_db_obj is None:
            global_db_obj = DBInit()
            log.info(f"global_db_obj created")
        return global_db_obj

    @staticmethod
    def get_db_connection():
        DataBaseObj.init_db_obj()
        global db_connection
        if db_connection is None:
            db_connection = global_db_obj.get_connection()
            log.info(f"db_connection created")
        return db_connection

    @staticmethod
    def get_db_session():
        DataBaseObj.init_db_obj()
        global db_session
        if db_session is None:
            db_session = global_db_obj.get_session()
            log.info(f"db_session created")
        return db_session
