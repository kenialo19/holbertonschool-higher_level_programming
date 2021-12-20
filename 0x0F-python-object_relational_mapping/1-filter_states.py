#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1], password=argv[2], database=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

    state = cursor.fetchall()
    for state in state:
        print(state)

    cursor.close()
    db.close()
