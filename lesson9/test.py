import asyncio

from loguru import logger

delimiter = 100*'-'

secs = .2


async def foo():
    logger.info("async foo starting")
    await asyncio.sleep(secs*2)
    logger.info("async foo finishing")


async def bar():
    logger.info("async bar starting")
    await asyncio.sleep(secs)
    logger.info("async bar finishing")


async def run_async():
    logger.info("Start async")
    await foo()
    await bar()


def run_main_sync():
    logger.info('Starting main...')
    asyncio.run(run_async())
    logger.info('Finishing main...')


def run_main_async():
    logger.info('Starting main...')
    coroutines = [
        foo(),
        bar()
    ]
    tasks = asyncio.wait(coroutines)
    asyncio.run(tasks)
    logger.info('Finishing main...')


if __name__ == '__main__':
    run_main_sync()
    logger.info(delimiter)
    run_main_async()
