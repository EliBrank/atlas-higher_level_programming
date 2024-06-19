#!/usr/bin/python3

"""SQL query - retrieves all rows from states table

where name matches argument
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
        "SELECT * FROM states WHERE name LIKE '{}' "
        "ORDER BY states.id".format(state_name_searched)
    )

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    main()
