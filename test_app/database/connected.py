from dotenv import load_dotenv, dotenv_values

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


conf = dotenv_values(".env")
engine = create_engine(conf.get('DB'))
db_conn = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
sess = db_conn()

metadata = MetaData()
Base = declarative_base(metadata=metadata)
Base.query = db_conn.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
