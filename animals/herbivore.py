from animal import Animal

class Herbivore(Animal):
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        super().__init__(name, age, energy, weight, speed, skill, luck)
        
        
    
    def eat(self, meat: bool, food: int):
        if not meat:
            return super().eat(meat, food)
        else:
            print("I'm vegan")
    
    
    


