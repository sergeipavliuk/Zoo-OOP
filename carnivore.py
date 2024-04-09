from animal import Animal
from food import Food

class Carnivore(Animal):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)  
        
    def hunt(self, prey: Animal):
        if self.energy > 100:
            print('Naah, I am full enouth')
            return
        if self._speed*self._luck/100*self._skill/100 > prey._speed*prey._luck/100*prey._skill/100:
            print('The hunt was a success')
            self._energy += int(prey._energy/10)
            prey._energy = -1000
        else:
            self._energy -= 5
            prey._energy -= 5
   
    def eat(self, food: Food):
        print('Nom-nom')
        return super().eat(food)
    
    
    


