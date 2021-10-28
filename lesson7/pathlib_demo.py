from pathlib import Path

p = Path('/home/tolic')

print(f"repr('{p}'): {p.__repr__()}")
print(f"exists('{p}'): {p.exists()}")
print(f"parent of '{p}': {p.parent.__repr__()}")

# for key in dir(p):
#     if not key.startswith('_'):
#         print(f'{key}: {getattr(p,key)}')
