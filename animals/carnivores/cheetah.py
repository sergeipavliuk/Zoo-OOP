from animals.carnivore import Carnivore

class Cheetah(Carnivore):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        
        self._speed = self._speed + 100
        print(f'Cheetah {self._name} spowned')


ch = Cheetah("Speedy", 2, 100, 40, 100, 100, 100)