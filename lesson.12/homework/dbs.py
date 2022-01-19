import logging
from tortoise import Tortoise

from models import MyModel
import urls


async def init():
    await Tortoise.init(
        db_url="postgres://user:password@localhost/postgres",
        modules={'models': ['models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


async def create_obj_from_dict(cls: MyModel, params: dict):
    """
    Create/update object of MyModel class
    Update decision makes by searching object by key_fields
    :param cls: class of object to create/update
    :param params: data record to write in dict format
                   example: {'id': 1, 'name': 'Name1', ...}
    :return:
    """
    logging.info(f'Saving {cls}...')
    kwargs = {k: params[k] for k in cls.key_fields}
    defaults = {k: params[k] for k in cls.data_fields}
    await cls.update_or_create(defaults=defaults, using_db=None, **kwargs)
    logging.info(f'{cls} saved.')


async def load_obj_to_db(url: str, cls: MyModel):
    await create_obj_from_dict(
        cls,
        await urls.fetch_obj(url=url)
    )
