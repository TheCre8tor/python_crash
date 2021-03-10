class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # This is one way of doint it
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)  # This is another way of doing it
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.num_arrows}')


wizardOne = Wizard('Merlin', 50, 'merlin@gmail.com')
archerOne = Archer('Robin', 100, 'robin@gmail.com')
print(wizardOne.email)
print(archerOne.email)
# archerOne.attack() 


# Checking if a class is an instance of another class
# print(isinstance(wizardOne, User))
# print(isinstance(wizardOne, Archer))