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
    state_name = sys.argv[4]

    db_connect = MySQLdb.connect(
                                host='localhost',
                                port=3306,
                                user=username,
                                passwd=password,
                                db=db_name,
                                charset='utf8'
                                )

    cursor = db_connect.cursor()

    query = """SELECT cities.name \
                FROM cities \
                JOIN states ON states.id = cities.state_id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    state_cities = ''
    for row in rows:
        if state_cities == '':
            state_cities += str(row).strip('(),')
        else:
            state_cities += ', ' + str(row).strip('(),')
    print(state_cities)

    cursor.close()
    db_connect.close()
