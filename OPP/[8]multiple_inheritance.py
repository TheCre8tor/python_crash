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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print(f'ran really fast')


# This class has access to all the rest of the classes
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


borg = HybridBorg('HybridBorg', 200, 100)
print(borg.sign_in())
