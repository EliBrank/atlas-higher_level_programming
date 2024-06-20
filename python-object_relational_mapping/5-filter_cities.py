#!/usr/bin/python3

"""SQL query - retrieves all cities from the database hbtn_0e_4_usa

data is displayed in a comma-separated list
"""

import MySQLdb
from sys import argv


def main():
    """creates SQL query"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    state_name_searched = argv[4]

    c = db.cursor()

    c.execute(
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name LIKE %s "
        "ORDER BY cities.id", (state_name_searched,)
    )

    rows = c.fetchall()
    list_output = []
    for row in rows:
        list_output += row

    print(", ".join(list_output))

    c.close()
    db.close()


if __name__ == "__main__":
    main()
