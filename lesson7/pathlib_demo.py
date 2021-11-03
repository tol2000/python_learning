import os
import pathlib
from pathlib import Path

home = Path('/home/tolic')

print(f"repr('{home}'): {home.__repr__()}")
print(f"exists('{home}'): {home.exists()}")
print(f"parent of '{home}': {home.parent.__repr__()}")

# for key in dir(p):
#     if not key.startswith('_'):
#         print(f'{key}: {getattr(p,key)}')

down = Path('Download')

pa = home / down / 'torrents'

print(pa / "111" / "222")
