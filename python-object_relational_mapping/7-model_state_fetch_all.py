#!/usr/bin/python3

"""defines the function model_state_fetch_all"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def model_state_fetch_all():
    """lists all state objects for specified database"""

    user = argv[1]
    password = argv[2]
    host_name = 'localhost'
    db_name = argv[3]

    engine_base = 'mysql+mysqldb://{}:{}@{}:3306/{}'

    engine = create_engine(
        engine_base.format(user, password, host_name, db_name)
    )

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        states = session.query(State).order_by(State.id)
        for state in states:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    model_state_fetch_all()
