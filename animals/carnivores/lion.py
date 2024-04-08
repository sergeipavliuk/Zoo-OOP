from carnivore import Carnivore

class Lion(Carnivore):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        print(f'Lion {self._name} spowned')
