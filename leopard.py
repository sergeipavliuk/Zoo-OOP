from carnivore import Carnivore

class Leopard(Carnivore):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        
        self._speed = self._speed + 50
        print(f'Leopard {self._name} spowned')

    def __str__(self) -> str:
        return f'I am a leopard {super().__str__()}'