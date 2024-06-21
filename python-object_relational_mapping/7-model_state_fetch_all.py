#!/usr/bin/python3
"""
return all state objects from database via python
parameters given to script: username, password, database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Ensure correct number of command-line arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Retrieve command-line arguments
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    # Create engine for connecting to the database
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all State objects and print their id and name
        for instance in session.query(State).order_by(State.id):
            print(f"{instance.id}: {instance.name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
