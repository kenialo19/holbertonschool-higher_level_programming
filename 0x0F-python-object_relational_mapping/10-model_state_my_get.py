#!/usr/bin/python3
"""Write a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    id_position = argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    db = session.query(State).order_by(State.id).filter(State.name == id_position).first()
    if db is None:
        print('Not found')
    else:
        print("{}".format(db.id))

    session.close()
