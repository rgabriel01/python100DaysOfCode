import psycopg2
import ipdb

class PyDb:

    def __init__(self):
        self.conn = psycopg2.connect("dbname='carabao_development' user='raymondgabriel' host='localhost'")

    def yo(self):
        cur = self.conn.cursor()
        cur.execute("select id, email "
                    "from leads "
                    "where leads.email is not null "
                    "limit 10")
        rows = cur.fetchall()
        for row in rows:
            print("Fetching records for ", row[0], row[1])

PyDb().yo()
