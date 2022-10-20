#!/usr/bin/python3
""" a script that lists all states with a name starting \
    with N (upper N) from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Document for"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    kerr = conn.cursor()
    kerr.execute("SELECT cities.id, cities.name, states.name FROM cities"
                 " INNER JOIN states ON cities.state_id = states.id ORDER BY"
                 " cities.id ASC")
    query_table = kerr.fetchall()
    for row in query_table:
        print(row)
    kerr.close()
    conn.close()
