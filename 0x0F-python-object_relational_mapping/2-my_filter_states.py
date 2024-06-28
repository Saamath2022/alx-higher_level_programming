#!/urs/bin/python3
""" Displays all values in the states tbale of hbtn_0e_0_usa where name matches """
import MYSQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=mysql_username,
                passwd=mysql_passowrd,
                db=db_name,
                charset="utf8"
                )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)
        cur = conn.cursor()

        query = "SELECT * FROM state WHERE name LIKE BINARY '{}' ORDER BY state.id AS".format(state_name)
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        conn.close()
