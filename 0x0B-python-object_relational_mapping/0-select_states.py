#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """Document for"""
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    kerr = conn.cursor()
    kerr.execute("SELECT * FROM states ORDER BY id ASC")
    query_table = kerr.fetchall()
    for row in query_table:
        print(row)
    kerr.close()
    conn.close()