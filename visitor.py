from food import Food
from animal import Animal

class Visitor():
    def __init__(self, name: str) -> None:
        self.name = name
        print(f'Visitor {self.name} spowned')

    def feed(self, food: Food, animal: Animal):
        animal.eat(food)