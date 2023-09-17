#!/usr/bin/python3
'''
Module to display states from hbtn_0e_0_usa database
'''
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_connect = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=db_name, charset='utf8')

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()

