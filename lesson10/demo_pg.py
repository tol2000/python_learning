from datetime import datetime
from pprint import pprint

import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="user",
    password="password",
)

print(conn)
cur = conn.cursor()

print(cur)

res = cur.execute("SELECT id, full_name, username FROM users;")
pprint(res)

users = cur.fetchall()
pprint(users)

dt = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
res = cur.execute(f"INSERT INTO users (username, full_name) VALUES ('sam_{dt}', 'Sam was born in {dt}');")
print(conn.commit())


conn.close()
