# List is an ordered sequence of object that can be any type
li = [1, 2, 3, 4, 5];
li2 = ['a', 'b', 'c', 'd', 'e'];
li3 = [1, 2, 3, 'f', True, False];

# List is one of Python Data Structure

amazon_cart = [ #list a Mutable
    'Notebook', 
    'Sunglasses',
    'Toys',
    'Grapes'
];  
  
returned = amazon_cart[0:3:2]
step = amazon_cart[0::2]
# print(step)

amazon_cart[0] = 'Laptop'
# NOTE: Anytime we do "list slicing", we create a copy of that list.
new_cart = amazon_cart[:]  # This is a copy version
# new_cart = amazon_cart  # The new_cart variable is the representator of the amazon_cart 
new_cart[0] = 'Gum'
# print(new_cart)
# print(amazon_cart)


# Inserting an Item in a list
ramdoma = []

ramdoma.append('2') 
ramdoma.append(5)
ramdoma.append('Me') 
# print(ramdoma)


