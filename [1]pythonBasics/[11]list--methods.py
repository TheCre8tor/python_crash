# --- LIST METHODS ---
# Python List/Array Methods --> https://www.w3schools.com/python/python_ref_list.asp

basket = ['a', 'b', 'x', 'c', 'd', 'e', 'd']

# basket.sort()  # This method Sort the list in ascending order and return None.
sortedFunc = sorted(basket) # This function return a new list containing all items from the iterable in ascending order.
plate = basket.copy() # This method copy's the list
plate.sort()
plate.reverse()
# print(sortedFunc) 
# print(basket) 
# print(plate)


# ADDING --> This methods add objects to the list
basketInt = [1, 2, 3, 4, 5]

# basketInt.append(100)
# basketInt.insert(0, 200);  # Insert modify the List in place, it does not copy it.
# basketInt.extend([50, 40, 30, 20, 50, 50]) # This method extends the existen List

# print(basketInt)


# REMOVING --> This methods removes objects from the list
# basketInt.pop()  # Remove and return item at index (default last)
# value = basketInt.pop(0)  # It can also remove item from any index location
# print(basketInt)
# print(value)  # NOTE: pop() returns whatever we just remove.

# basketInt.remove(50)  # Remove first occurrence of value.
# print(basketInt)

# basketInt.clear()  # Removes all items from list.
# print(basketInt)


# INDEX
basketInt = ['a', 'b', 'c', 'd', 'b', 'e', 'b']
# print(basketInt.index('b'))
print('x' in basketInt)
print('i' in 'hi my name is Ian')
print(basketInt.count('b'))


# --- TEST QUIZ ---
# using this list, 
bucket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
bucket.pop(0)

# 2. Remove "Blueberries" from the list.
bucket.pop()

# 3. Put "Kiwi" at the end of the list.
bucket.append('Kiwi')

# 4. Add "Apples" at the beginning of the list
bucket.insert(0 ,'Apples')

# 5. Count how many apples in the bucket
apple_bucket = bucket.count('Apples')

# 6. empty the bucket
bucket.clear()

# print(apple_bucket)
# print(bucket)


## ------ -->
lister = list(range(0,102, 2))
# print(lister)

getArray = ['I', 'my', 'name', 'is', 'Alexander']
name = ' '.join(getArray)
# print(name)


# LIST UNPACKING / DESTRUCTURING
small, medium, big, *rest, last = ['sm', 'md', 'bg', 'ssm', 'smd', 'sbg', 'large']

print(small)
print(medium)
print(rest)
print(last)