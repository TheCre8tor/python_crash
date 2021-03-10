class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    # We basically change the meaning of 
    # the str method it doesn't change things
    # except within action_figure
    def __str__(self): 
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'methon call!'

    def __getitem__(self, idx):
        return self.my_dict[idx]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())  # This works with the __call__ dunder method
print(action_figure['name'])
