import os
import sys
import datetime
# import pytz
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

# Create an engine that stores data in the local directory's
# dojo_rooms.db file.
engine = create_engine('sqlite:///dojo_rooms.db', echo=False) # disable logging with False
Base = declarative_base()

# eat_timezone = pytz.timezone('Africa/Nairobi')

class DbOffices(Base):
    """Here we define columns for the table offices"""

    __tablename__ = "offices"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    staff = relationship("DbStaff", backref="offices")
    fellows = relationship("DbFellows", backref="offices")
    date_created = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name):
        self.name = name


class DbLivingSpaces(Base):
    """Here we define columns for the table livingspaces"""

    __tablename__ = "livingspaces"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fellows = relationship("DbFellows", backref="livingspaces")
    date_created = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name):
        self.name = name

class DbStaff(Base):
    """Here we define columns for the table staff"""

    __tablename__ = "staff"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    office = Column(Integer, ForeignKey("offices.id"), nullable=True)
    date_created = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name, office):
        self.name = name
        self.office = office

class DbFellows(Base):
    """Here we define columns for the table fellows"""

    __tablename__ = "fellows"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    office = Column(Integer, ForeignKey("offices.id"), nullable=True)
    livingspace = Column(Integer, ForeignKey("livingspaces.id"), nullable=True)
    wants_accommodation = Column(String, nullable=False, default='N')
    date_created = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name, office, livingspace, wants_accommodation):
        self.name = name
        self.office = office
        self.livingspace = livingspace
        self.wants_accommodation = wants_accommodation

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
