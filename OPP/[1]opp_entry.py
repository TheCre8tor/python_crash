# A method is a function in an object.

class PlayerCharacter:
    membership = True  # Class Attribute

    # Constructor Function
    # This constructor is called anytime we instantiate an object
    def __init__(self, name="Anonymous", age=20):
        # print(help(self))
        if age > 18:
            self.name = name  # Instance attribute
            self.age = age  # Instance attribute

    def run(self):
        return f'My name is {self.name}'

    def question(self, param):
        return f'Why have you been working so {param} lately? {self.name}'

    # Creating Class Method
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things1(num1, num2):
        return num1 + num2


playerOne = PlayerCharacter('Alexander', 26)
# playerTwo = PlayerCharacter('Juliet', 37)
# playerOne = PlayerCharacter()
# playerTwo = PlayerCharacter('Samuel', 10)

# playerTwo.attack = 'Kill them all'

print(playerOne.run())
# print(playerOne.question('hard'))

# print(playerOne.question('hard'))

# print(playerTwo.attack)
# print(playerOne.membership)
# print(PlayerCharacter.adding_things(5, 10))

