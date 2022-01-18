import asyncio
import asyncpg
from datetime import date

delimiter = 150*'-'


async def main():
    conn = await asyncpg.connect(
        "postgresql://user:password@localhost/postgres"
        # user='user',
        # password='password',
        # database='database',
        # host='127.0.0.1'
    )

    await conn.execute('truncate table users')

    await conn.execute(
        "INSERT INTO users(name, birth_date) VALUES($1, $2)",
        # "INSERT INTO users(name, birth_date) VALUES(?, ?)",
        "John",
        date(1972, 3, 15),
    )

    await conn.execute(
        "INSERT INTO users(name, birth_date) VALUES($1, $2)",
        # "INSERT INTO users(name, birth_date) VALUES(?, ?)",
        "Ann",
        date(1976, 6, 15),
    )

    await conn.execute(
        "INSERT INTO users(name, birth_date) VALUES($1, $2)",
        # "INSERT INTO users(name, birth_date) VALUES(?, ?)",
        "James",
        date(1977, 7, 21),
    )

    await conn.execute(
        "INSERT INTO users(name, birth_date) VALUES($1, $2)",
        # "INSERT INTO users(name, birth_date) VALUES(?, ?)",
        "Толян",
        date(1973, 7, 9),
    )

    rows = await conn.fetch("SELECT id, name, birth_date FROM users;")
    print(rows)
    today = date.today()
    for r in rows:
        print(f'{r["id"]}, {r["name"]}, {int((today - r["birth_date"]).days/365)} y.o.')

    print(delimiter)
    john: asyncpg.Record = await conn.fetchrow("SELECT * FROM users WHERE name = $1", "John")
    print(list(john.items()))

    # values = await conn.fetch()
    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
