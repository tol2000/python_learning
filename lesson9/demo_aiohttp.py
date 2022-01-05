import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger


@dataclass()
class Service:
    name: str
    url: str
    ip_field: str


SERVICES = [
    Service(name='ipify', url='https://api.ipify.org/?format=json', ip_field='ip'),
    Service(name='ip-api', url='http://ip-api.com/json', ip_field='query')
]


async def fetch(c_session, url) -> dict:
    """

    :param c_session:
    :param url:
    :return:
    """
    async with c_session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    """

    :param service:
    :return:
    """
    try:
        async with ClientSession() as session:
            result = await fetch(session, service.url)
        logger.info(f"Got result for {service.name}, result {result}")
        my_ip = f'{result[service.ip_field]} from {service.name}'
        # if service.name == 'ip-api':
        #     raise IOError
        # if service.name == 'ipify':
        #     raise IOError
    except Exception as ex:
        # my_ip = None
        # Entering in endless loop to get other coroutines return right answer :)
        # If all coroutines will enter into the endless loop then wait() function
        #   will end with timeout
        logger.exception(ex)
        while True:
            await asyncio.sleep(1)
    return my_ip


def get_my_ip():
    coros = [fetch_ip(s) for s in SERVICES]
    tasks = asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED, timeout=5)
    result = None
    # first time processing until the first task completed
    logger.info('First run')
    done, pending = asyncio.run(tasks)
    for task in done:
        task_result = task.result()
        if task_result:
            result = task_result
            break
    for task in pending:
        task.cancel()
    return result


def run_main():
    ip = get_my_ip()
    logger.info(f'ip: {ip}')


if __name__ == '__main__':
    run_main()
