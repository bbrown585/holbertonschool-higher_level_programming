#!/usr/bin/python3
""" a script that lists all states with a name starting \
    with N (upper N) from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Document for"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    kerr = conn.cursor()
    query = "SELECT cities.name FROM cities"
    query = query + " INNER JOIN states ON cities.state_id = states.id"
    query = query + " WHERE states.name = %s ORDER BY cities.id ASC"
    kerr.execute(query, [sys.argv[4]])
    query_table = kerr.fetchall()
    print(", ".join([row[0] for row in query_table]))
    kerr.close()
    conn.close()
