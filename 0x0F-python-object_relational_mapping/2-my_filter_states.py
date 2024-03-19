#!/usr/bin/python3
'''
list_states function
'''
import sys
import MySQLdb


def list_states(username, password, database_name, name_searched):
    '''
    A function that takes kwargs to pass to the MySQLdb module

    Args:
        username (str): username of the database user
        password (str): password of the database user
        database_name (str): name of the database to query from
    '''
    # connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # create a cursor object using cursor() method
    cursor = db.cursor()

    # vulnerable SQL query
    sql_query = f"SELECT * FROM states WHERE name = '{name_searched}'"

    # execute the SQL command
    cursor.execute(sql_query)
    # fetch all the rows
    results = cursor.fetchall()

    # display the results
    for row in results:
        print(row)

    # close the database connection
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    input = sys.argv[4]

    list_states(username, password, database_name, input)
