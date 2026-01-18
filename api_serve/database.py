from sqlalchemy import create_engine,Column,Integer,String,DateTime,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DATABASE_URL="sqlite:///.movie_reccomender.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread':False} if 'sqlite' in DATABASE_URL else {}
)

sessionlocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()

class SearchHistory(Base):

    """Table that tracks every single search made by user"""
    __tablename__="search_history"
    id=Column(Integer,primary_key=True,index=True)
    movie_searched=Column(String)
    reccomendations=Column(Text)
    movie_name=Column(String)
    timestamp=Column(DateTime,default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("All the tables have been created")

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()