#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1], password=argv[2], database=argv[3], port=3306)
    cursor = db.cursor()
    argument = argv[4]
    cursor.execute(
        'SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name=%(argument)s ORDER BY cities.id ASC',
        {'argument': argument})
    city = []
    for state in cursor.fetchall():
        city.append(state[1])
    print(', '.join(city))
    cursor.close()
    db.close()
