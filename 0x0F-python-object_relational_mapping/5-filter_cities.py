#!/usr/bin/python3
'''list_cities function
'''
import sys
import MySQLdb


def list_cities(username, password, database_name, name_searched):
    '''
    A function that lists all cities from the a database

    Args:
        username (str): username of database user
        password (str): password of database user
        database_name (str): name of database
    '''
    # connect to MySQL serevr
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # create a cursor object using cursor() method
    cursor = db.cursor()

    # SQL query
    sql_query = (
        'SELECT name '
        'FROM cities '
        'WHERE state_id = '
        '(SELECT id '
        'FROM states '
        'WHERE name = %s) '
        'ORDER BY cities.id ASC;'
    )

    # execute the query
    cursor.execute(sql_query, (name_searched,))

    # fetch all rows
    results = cursor.fetchall()

    # display the results
    lst = []
    for row in results:
        lst.append(row[0])
    res_str = ', '.join(lst)
    print(res_str)

    # close the connection
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    input = sys.argv[4]

    list_cities(username, password, database_name, input)
