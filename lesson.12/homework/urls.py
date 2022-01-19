import logging
from dataclasses import dataclass

from aiohttp import ClientSession

from models import *

domain = 'https://jsonplaceholder.typicode.com'


@dataclass()
class Obj2Get:
    obj_class: MyModel
    url: str
    qnty: int


# noinspection PyTypeChecker
objs2get = [
    # 10, 100, 100, 200, 500, 5000
    Obj2Get(User, '/users', 1),
    Obj2Get(Post, '/posts', 1),
    Obj2Get(Album, '/albums', 1),
    Obj2Get(ToDo, '/todos', 1),
    Obj2Get(Comment, '/comments', 1),
    Obj2Get(Photo, '/photos', 5),
]


async def fetch_obj(url) -> dict:
    """
    returns json obj from url
    :param url:
    :return:
    """
    logging.info(f'Loading from {url}...')
    async with ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
    logging.info(f'{url} loaded.')
    return res
