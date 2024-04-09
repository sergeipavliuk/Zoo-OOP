from animal import Animal
from food import Food

class Herbivore(Animal):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int, defence:int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        self._defence = defence
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nDefence = {self.defence}'
        
    @property
    def defence(self) -> int:
        return self._defence
    
    def eat(self, food: Food):
        if food.vegan:
            return super().eat(food)
        else:
            print("I'm vegan")

    def hunt(self, prey:Animal):
        print(f'Oh, you are not a carrot, sorry dear {prey.name}')
        #return super().hunt()

    
    



