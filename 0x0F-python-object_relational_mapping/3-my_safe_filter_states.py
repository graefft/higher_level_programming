#!/usr/bin/python3
'''Script that lists states from database hbtn_0e_0_usa matching argument'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2],
                               db=argv[3])

    c = database.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
              [argv[4]])
    data = c.fetchall()
    for row in data:
        print(row)
    c.close()
    database.close()
