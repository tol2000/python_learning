import asyncio

from sqlalchemy.dialects import postgresql
from tabulate import tabulate
import asyncpg

from asyncpgsa import pg
from sqlalchemy import MetaData, Table, Column, Integer, String, Date

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("birth_date", Date, nullable=False),
)


def left_pad(text: str, min_length: int) -> str:
    if len(text) < min_length:
        text = " " * (min_length - len(text)) + text
    return text


# noinspection PyTypeChecker
async def exec_and_print(users_query):
    results: list[asyncpg.Record] = await pg.query(users_query)
    sql = str(users_query.compile(dialect=postgresql.dialect()))
    headers = [c.name for c in users_table.columns]
    out = []
    for item in results:
        cols = [str(x) for x in item.values()]
        out.append(cols)
    print()
    print(sql)
    print(
        tabulate(tabular_data=out, headers=headers, tablefmt='orgtbl')
    )


async def main():
    await pg.init(
        "postgresql://user:password@localhost/postgres"
        # host=HOST,
        # port=PORT,
        # database=DB_NAME,
        # user=USER,
        # # loop=loop,
        # password=PASS,
        # min_size=5,
        # max_size=10
    )

    # users_query = users_table.select()
    # results: asyncpg.Record = await pg.query(users_query)
    # for index, row in enumerate(results):
    #     if index == 0:
    #         print(" | ".join([left_pad(name, 13) for name in row.keys()]))
    #     print(" | ".join([left_pad(str(value), 13) for value in row.values()]))
    #
    # james = await pg.fetchrow(users_query.where(users_table.c.name == "James"))
    # print()
    # print(james)

    users_query = users_table.select()
    await exec_and_print(users_query)
    users_query = users_table.select().where(users_table.c.name == 'Толян')
    await exec_and_print(users_query)


if __name__ == '__main__':
    asyncio.run(main())
