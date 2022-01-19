import asyncio

from tortoise import run_async
import logging

import urls
import dbs
import config


async def main():
    await dbs.init()

    logging.info(f'Creating tasks...')
    tasks = []
    for obj in urls.objs2get:
        for i in range(1, obj.qnty+1):
            tasks.append(
                asyncio.create_task(
                    dbs.load_obj_to_db(
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
