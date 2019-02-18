import arrow
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Sets up the database for spider
Base = declarative_base()
engine = create_engine('sqlite:///data.db',
    connect_args={'check_same_thread':False},
    poolclass=StaticPool
)
Base.metadata.bind = engine

class UniqueKey(Base):
    __tablename__ = 'unique_keys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
    created = Column(DateTime, default=arrow.utcnow().datetime)

create_session = sessionmaker(bind=engine)

# Used once to create database
Base.metadata.create_all(engine)
