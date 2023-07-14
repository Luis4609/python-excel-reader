import pymysql

conn = pymysql.connect(
    host='localhost:3306',
    user='root',
    password='root',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# read data from DB
try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
finally:
    conn.close()