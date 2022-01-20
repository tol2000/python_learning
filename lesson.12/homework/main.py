import asyncio

from aiohttp import ClientSession
from tortoise import run_async
import logging

import urls
import dbs
from my_models import MyModel
import config


async def load_obj_to_db(session: ClientSession, url: str, cls: MyModel):
    try:
        await dbs.create_obj_from_dict(
            cls,
            await urls.fetch_obj(session=session, url=url)
        )
    except Exception as ex:
        if not config.debug:
            logging.error(f'Exception on url {url}: {ex}')
        else:
            logging.exception(f'Exception on url {url}')


async def main():
    await dbs.init()

    logging.info(f'Creating tasks...')
    tasks = []
    async with ClientSession() as session:
        for obj in urls.objs2get:
            for i in range(1, obj.qnty+1):
                tasks.append(
                    asyncio.create_task(
                        load_obj_to_db(
                            session=session,
                            url=f'{urls.domain}{obj.url}/{i}',
                            cls=obj.obj_class
                        )
                    )
                )
        logging.info(f'Executing tasks...')
        await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


if __name__ == "__main__":
    logging.info(f'Starting, logging to {config.log_filename_with_path}...')
    run_async(main())
