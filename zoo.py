import random
from animal import Animal
from carnivore import Carnivore
from herbivore import Herbivore
from visitor import Visitor
from food import Food

class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []
        self.visitors: list[Visitor] = []
        self.food: list[Food] = []

    def add_animal(self, animal:Animal):
        self.animals.append(animal)
        
    def add_visitor(self, visitor: Visitor):
        self.visitors.append(visitor)

    def add_food(self, food:Food):
        self.food.append(food)

    def consumpt(self):
        for animal in self.animals:
                animal.consumpt()

    def sleep(self):
        for animal in self.animals:
                animal.sleep()
                print(f'{animal.name} the {animal.__class__.__name__} is sleeping')

    def bring_out_your_dead(self):
        self.animals = [animal for animal in self.animals if animal.energy > 0]

    def day_sim(self, day: int):
        print(f"\n\n############# Day № {day} begins")

        
        for animal in self.animals:
            

            try:
                if isinstance(animal, Carnivore):
                    random_prey = random.choice([pr for pr in self.animals if isinstance(pr, Herbivore) ])
                    print(f"{animal.name} the {animal.__class__.__name__} is going to hunt {random_prey.name} the {random_prey.__class__.__name__}")
                    animal.hunt(random_prey)
            except:
                print("There are no more herbivores left, lets eat others")
                if isinstance(animal, Carnivore):
                    random_prey = random.choice([pr for pr in self.animals])
                    print(f"{animal.name} the {animal.__class__.__name__} is going to hunt {random_prey.name} the {random_prey.__class__.__name__}")
                    animal.hunt(random_prey)        
                
            animal.graze()
            print(f"{animal.name} the {animal.__class__.__name__} is grazing and has {animal.energy} energy")

        for visitor in self.visitors:
            for i in range(3):
                random_animal = random.choice(self.animals)
                random_food = random.choice(self.food)
                visitor.feed(random_food,random_animal)
                print(f'Visitor {visitor.name} is feeding {random_animal.name} the {random_animal.__class__.__name__}')

        self.consumpt()
        self.bring_out_your_dead()
        self.sleep()

        
        
