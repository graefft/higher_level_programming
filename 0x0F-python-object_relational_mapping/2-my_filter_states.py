#!/usr/bin/python3
'''Script that lists states from database hbtn_0e_0_usa matching argument'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    query = query.format(argv[4])
    c.execute(query)
    data = c.fetchall()
    for row in data:
        print(row)
    c.close()
    database.close()
