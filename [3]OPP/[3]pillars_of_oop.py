# 4 PILLARS OF OOP

# 1. Encapsulation --> Encapsulation is the binding of data and functions that manipulate the data.
class SimplyMethod:
    # Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def run_js(self):
        return f'{self.name} is strong'


get_data = SimplyMethod('Alexander', 26)
print(get_data.run_js())


# 2. Abstraction --> Hiding of information or hiding away information and giving access to only what's necessary.
class AbstractAway:
    # Attributes
    def __init__(self, name, age):
        self._name = name
        self._age = age

        # By using the _ character we are creating a private attribute.

    # Methods
    def run_js(self):
        return f'{self._name} is strong'

    
# 3. Inheritance --> Inheritance allow new objects to take on the properties of existen object.
 
# NOTE: If we don't have any variables, or attributes that we want to assign, to the user, then we don't need the __init__
class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')


wizardOne = Wizard('Merlin', 50)
# archerOne = Archer('Robin', 100)
# wizardOne.attack()
# archerOne.attack() 


# Checking if a class is an instance of another class
print(isinstance(wizardOne, User))
print(isinstance(wizardOne, Archer))


# 4. Polymorphism --> Polymorphism means many forms, meaning different classes can share the same method names