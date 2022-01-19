from tortoise import Tortoise, run_async, fields
from tortoise.models import Model


class Tournament(Model):
    class Meta:
        table = 'tournaments'

    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        attrs = ['id', 'name']
        attrs_str = ', '.join([f'{k}={self.__getattribute__(k)}' for k in attrs])
        return f'{self.__class__.__name__}({attrs_str})'


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url="postgres://user:password@localhost/postgres",
        modules={'models': ['__main__']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def main():
    await init()

    # tournament = Tournament(name='New Tournament')
    # await tournament.save()

    await Tournament.update_or_create(defaults={'name': 'Another Tournament'}, using_db=None, id=1)
    await Tournament.update_or_create(defaults={'name': 'Tournament Толяна'}, using_db=None, id=2)
    await Tournament.update_or_create(defaults={'name': 'Tournament Коляна'}, using_db=None, id=3)
    await Tournament.update_or_create(defaults={'name': 'Tournament всех турнаментов'}, using_db=None, id=4)

    # Now search for a record
    for tour in await Tournament.filter(name__contains='оляна').all():
        print(tour.id, tour.name)

    for t in await Tournament.all():
        print(t)


if __name__ == "__main__":
    # run_async is a helper function to run simple async Tortoise scripts.
    # run_async(init())
    run_async(main())
