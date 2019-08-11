#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    data = c.fetchall()
    for row in data:
        if row[1].startswith("N"):
            print(row)
    c.close()
    database.close()
