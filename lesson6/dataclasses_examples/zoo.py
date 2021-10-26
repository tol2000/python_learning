from dataclasses import dataclass, field
from animals import Bear

#
# class Zoo:
#
#     def __init__(self, animals):
#         self.animals = animals
from typing import List


@dataclass
class Zoo:
    animals: List[Bear] = field(default_factory=list)
    # animals: List[Bear] = []
