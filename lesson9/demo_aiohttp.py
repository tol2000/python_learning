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
        if service.name == 'ip-api':
            raise IOError
        # if service.name == 'ipify':
        #     raise IOError
    except:
        my_ip = None
    return my_ip


def get_my_ip():
    coros = [fetch_ip(s) for s in SERVICES]
    tasks = asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)
    result = None
    # first time processing until the first task completed
    logger.info('First run')
    done, pending = asyncio.run(tasks)
    for task in done:
        task_result = task.result()
        if task_result:
            result = task_result
            break
    while not result:
        # processing other tasks if first completed did not give result
        logger.info('First result is None. Next run')
        if pending:
            tasks = asyncio.wait(
                [
                    x.get_coro() for x in pending
                ],
                return_when=asyncio.FIRST_COMPLETED
            )
            done, pending = asyncio.run(tasks)
            for task in done:
                task_result = task.result()
                if task_result:
                    result = task_result
                    break
    return result


def run_main():
    ip = get_my_ip()
    logger.info(f'ip: {ip}')


if __name__ == '__main__':
    run_main()
