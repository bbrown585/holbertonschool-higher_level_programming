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
    kerr.execute(
        "SELECT * FROM states WHERE Name LIKE BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]))
    query_table = kerr.fetchall()
    for row in query_table:
        print(row)
    kerr.close()
    conn.close()
