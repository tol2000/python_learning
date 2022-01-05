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
    except:
        my_ip = None
    return my_ip


def get_my_ip():
    coros = [fetch_ip(s) for s in SERVICES]
    task = asyncio.wait(coros, return_when=asyncio.ALL_COMPLETED)
    done, pending = asyncio.run(task)
    # next time: set first_completed and
    #   while first completed task is None loop for all pending...
    result = 'Not found from all'
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
