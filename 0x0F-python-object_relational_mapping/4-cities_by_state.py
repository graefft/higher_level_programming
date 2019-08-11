#!/usr/bin/python3
'''Script that lists all cities from database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities " +
              "INNER JOIN states on cities.state_id = states.id " +
              "ORDER BY id ASC")
    data = c.fetchall()
    for row in data:
        print(row)
    c.close()
    database.close()
