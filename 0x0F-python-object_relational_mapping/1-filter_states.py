#!/usr/bin/python3
'''
Module to  lists all states with a name
starting with N (upper N) from the database
hbtn_0e_0_usa
'''
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_connect = MySQLdb.connect(
                                    host='localhost',
                                    port=3306,
                                    user=username,
                                    passwd=password,
                                    db=db_name,
                                    charset='utf8'
                                )

    cursor = db_connect.cursor()

    query = f"SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()
