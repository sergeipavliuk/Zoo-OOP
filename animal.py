import random
from food import Food
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

    def __str__(self) -> str:
        return f'\nName = {self.name}\nAge = {self.age}\nEnergy = {self.energy}\nWeight = {self.weight}\nSpeed = {self.speed}\nSkill = {self.skill}\nLuck = {self.luck}'

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

    def graze(self):
        self._energy += 10
        
    def eat(self, food: Food):
        if self.energy < 100:
            self._energy += food.energy
            print('Nom-nom')
        else:
            print("Neah, I'm full")

    def hunt(self):
        self._energy -= 5

    def sleep(self):
        self._energy += 10
        print(f'Zzz...    energy = {self.energy}')

    def consumpt(self):
        self._energy -= 15

    def make_sound(self):
        print('Basic animal sound')

