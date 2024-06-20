#!/usr/bin/python3

"""defines the function model_city_fetch_by_state"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv


def model_city_fetch_by_state():
    """deletes State objects with name containing a"""

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
        location = session.query(City, State).join(State).order_by(City.id)
        for city, state in location:
            print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    model_city_fetch_by_state()
