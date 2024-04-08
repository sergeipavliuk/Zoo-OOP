import random
class Animal():
    """Basic animal"""
    def __init__(self, name: str, age: int, energy: int, weight: int, speed: int, skill: int, luck: int) -> None:
        self._name = name
        self._age = age
        self._energy = energy
        self._weight = weight
        self._speed = speed
        if luck == -1: 
            luck = random.randint(30,100)
        self._luck = luck
        self._skill = skill     


    @property
    def name(self) -> int:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @property
    def energy(self) -> int:
        return self._energy
    
    @property
    def weight(self) -> int:
        return self._weight
    
    @property
    def speed(self) -> int:
        return self._speed
    
    @property
    def skill(self) -> int:
        return self._skill
    
    @property
    def luck(self) -> int:
        return self._luck
        
    def spown(self):
        print("Hi, I'm a basic animal")
        
    def eat(self, meat:bool, food: int):
        self._energy += food

    def sleap(self):
        print('Zzz...')

    def make_sound(self):
        print('Basic animal sound')

b = Animal('b', 1, 50, 500, 10, 100, -1)
print(b.luck)
b.spown()