from animal import Animal

class Carnivore(Animal):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)


        
        

    def hunt(self, prey: Animal):
        if self._speed*self._luck/100*self._skill/100 > prey._speed*prey._luck/100*prey._skill/100:
            print('The hunt was a success')
            self._energy += prey._energy/10
            prey.__del__()

          
        
    
    def eat(self, food: int):
        print('Nom-nom')
        return super().eat(food)
    
    
    


