import time
from functools import partial

p = partial(print, "On", f"\"{time.asctime()}\"", "printed:")

p(1)
p("e bebe")
p("spam", "and", "eggs")
