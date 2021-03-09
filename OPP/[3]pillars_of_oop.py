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

# 2. Abstraction --> Hiding of information or hiding away information and giving access to only what's necessary
