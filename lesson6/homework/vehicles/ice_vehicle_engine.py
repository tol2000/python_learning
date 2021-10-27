from dataclasses import dataclass


@dataclass(repr=False)
class ICEVehicleEngine:
    name: str
    volume: int
    cylinders: float
    rpm: int

    def __repr__(self):
        return f'{self.name} ({self.cylinders}cyl  {self.volume}l {self.rpm}rpm)'
