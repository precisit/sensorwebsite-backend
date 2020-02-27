import psycopg2


try:
    conn = psycopg2.connect("dbname='postgres' user='arnthor' host='sensordata.cqxmt2gpnzag.us-east-1.rds.amazonaws.com' port='5432' password='Precisit123'")
    cur = conn.cursor()
    try:
        cur.execute("""INSERT INTO measurements (id, val, sensor) VAlUES (2, 22, 'temperature sensor')""")
        cur.execute("""select * from measurements;""")
        print(cur.fetchall())
        conn.commit()
    except:
        print("Can't query database")
    cur.close()
    conn.close()
except:
    print("Unable to connect to the database")

