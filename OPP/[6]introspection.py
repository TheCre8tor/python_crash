# Introspection --> Introspection in computer
# programming means the ability to determine 
# the type of an object at runtime.

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


# introspection
wizard = Wizard('Marlin', 'Magic', 'merlin@gmail.com')
print(dir(wizard))
