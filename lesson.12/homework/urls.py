import logging
from dataclasses import dataclass

from my_models import *

domain = 'https://jsonplaceholder.typicode.com'


@dataclass()
class Obj2Get:
    obj_class: MyModel
    url: str
    qnty: int


# noinspection PyTypeChecker
objs2get = [
    # Totally photos = 5000
    Obj2Get(User, '/users', 10),
    Obj2Get(Post, '/posts', 100),
    Obj2Get(Album, '/albums', 100),
    Obj2Get(ToDo, '/todos', 200),
    Obj2Get(Comment, '/comments', 500),
    Obj2Get(Photo, '/photos', 5000),
]


async def fetch_obj(session, url) -> dict:
    """
    returns json obj from url
    :param session:
    :param url:
    :return:
    """
    logging.info(f'Loading from {url}...')
    async with session.get(url) as response:
        res = await response.json()
    logging.info(f'{url} loaded.')
    return res
