import faker
import random

from antilopa import Antilopa
from cheetah import Cheetah
from elefant import Elefant
from giraffe import Giraffe
from leopard import Leopard
from lion import Lion
from mouse import Mouse
from zebra import Zeebra
from visitor import Visitor
from food import Food
from zoo import Zoo

fake = faker.Faker()
zoo = Zoo()

print('\n##################### Spowning animals\n')

for i in range(10):
    zoo.add_animal(Antilopa(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(150,300), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100), defence= random.randint(20,70) ))
for i in range(3):
    zoo.add_animal(Cheetah(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(30,60), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100) ))
for i in range(10):
    zoo.add_animal(Elefant(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(1000,5000), speed = random.randint(20,50), skill = random.randint(1,100), luck = random.randint(1,100),defence= random.randint(20,70) ))
for i in range(10): 
    zoo.add_animal(Giraffe(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(1000,5000), speed = random.randint(20,50), skill = random.randint(1,100), luck = random.randint(1,100),defence= random.randint(20,70) ))
for i in range(4):    
    zoo.add_animal(Leopard(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(150,300), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100) ))
for i in range(4):
    zoo.add_animal(Lion(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(150,300), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100)))
for i in range(30):    
    zoo.add_animal(Mouse(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(150,300), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100), defence= random.randint(0,7)))
for i in range(10):    
    zoo.add_animal(Zeebra(name = fake.name().split()[0], age=random.randint(1,40), energy=random.randint(50,100), weight = random.randint(150,300), speed = random.randint(30,100), skill = random.randint(1,100), luck = random.randint(1,100), defence= random.randint(20,70)))

print('\n##################### Spowning visitors\n')
for i in range(20):
    zoo.add_visitor(Visitor(name = fake.name()))

print('\n##################### Spowning food\n')
for i in range(20):
    zoo.add_food(Food(random.choice([True, False]), random.randint(10,30)))

for i in range(5):
    zoo.day_sim(i)

print('\n##################### Greet the survivors\n')

for animal in zoo.animals:
        print(f'{animal.name} the {animal.__class__.__name__}: Energy = {animal.energy}')