from tortoise import Tortoise, run_async
from models import User, MyModel


async def init():
    await Tortoise.init(
        db_url="postgres://user:password@localhost/postgres",
        modules={'models': ['models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def create_obj_from_json(cls: MyModel, params: dict):
    """
    Create/update object of MyModel class
    Update decision makes by searching object by key_fields
    :param cls: class of object to create/update
    :param params: data record to write in dict format
                   example: {'id': 1, 'name': 'Name1', ...}
    :return:
    """
    kwargs = {k: params[k] for k in cls.key_fields}
    defaults = {k: params[k] for k in cls.data_fields}
    await cls.update_or_create(defaults=defaults, using_db=None, **kwargs)


async def main():
    await init()
    await create_obj_from_json(
        User,
        {
            "id": 1,
            "name": "Толянчик",
            "username": "tol2000",
            "email": "tol2000@gmail.com",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 55000",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
    )


if __name__ == "__main__":
    run_async(main())
