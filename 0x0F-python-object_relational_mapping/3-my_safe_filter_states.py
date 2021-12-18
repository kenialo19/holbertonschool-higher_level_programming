#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1], password=argv[2], database=argv[3], port=3306)
    cursor = db.cursor()
    argument = argv[4]
    cursor.execute(
        'SELECT * FROM states WHERE name= %(argument)s ORDER BY states.id ASC',
        {'argument': argument})

    state = cursor.fetchall()

    for state in state:
        print(state)
