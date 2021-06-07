import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm.session import sessionmaker



engine = sqlalchemy.create_engine("sqlite:///dbase.db")
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)



from .user import User