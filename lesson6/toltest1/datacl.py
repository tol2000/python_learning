from dataclasses import dataclass


@dataclass(frozen=True)
class Tol:
    v1: str
    v2: int

    def __post_init__(self):
        # some backdoor to avoid frozen is to use class props in post_init :))
        Tol.v3 = self.v2 + 1


tol = Tol('Molodets', 5)
# tol.v2 = 11
# tol.v3 = 55

print(tol)

# looks like an object property :))
print(tol.v3)
