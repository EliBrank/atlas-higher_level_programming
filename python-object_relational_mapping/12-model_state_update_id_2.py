#!/usr/bin/python3

"""defines the function model_state_update_id_2"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def model_state_update_id_2():
    """updates State object with id of 2 to New Mexico"""

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
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = 'New Mexico'
            session.commit()


if __name__ == "__main__":
    model_state_update_id_2()
