from herbivore import Herbivore

class Antilopa(Herbivore):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        print(f'Antilopa {self._name} spowned')