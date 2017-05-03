import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Binary

# Create an engine that stores data in the local directory's
# dojo_rooms.db file.
engine = create_engine('sqlite:///dojo_rooms.db', echo=False) # disable logging with False
Base = declarative_base()

class DojoState(Base):
    __tablename__ = 'dojo_state'
    # Here we define columns for the table dojo_state
    # Notice that each column is also a normal Python instance attribute.

    id = Column(Integer, primary_key=True)
    dojo_state_name = Column(String)
    dojo_state_file = Column(Binary)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
