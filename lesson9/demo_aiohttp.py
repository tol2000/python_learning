import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

@dataclass()
class Service:
    name: str
    url: str
    ip_field: str

SERVICES = [
    Service(name='ipify', url='https://api.ipify.org/?format=json', ip_field='ip')
    Service(name='ipify', url='https://api.ipify.org/?format=json', ip_field='ip')
]
