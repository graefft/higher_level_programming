#!/usr/bin/python3
'''Script that lists all cities from database hbtn_0e_4_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    c.execute("SELECT cities.name FROM cities " +
              "INNER JOIN states ON cities.state_id = states.id " +
              "WHERE states.name LIKE BINARY %s " +
              "ORDER BY cities.id ASC", [argv[4]])
    data = c.fetchall()
    print(", ".join([row[0] for row in data]))
    c.close()
    database.close()
