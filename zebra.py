from herbivore import Herbivore
class Zeebra(Herbivore):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int, defence: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck, defence)
        print(f'Zeebra {self._name} spowned')
        

    def __str__(self) -> str:
        return f'I am a zeebra{super().__str__()}'