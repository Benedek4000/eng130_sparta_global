# Lists
# a list can contain values with different datatypes
spices = ['allspice', 'bay leaves', 'saffron', 'cinnamon', 'dill']
print(spices)
spices.append('vanilla')  # add item to list
print(spices)
spices[3] = 'turmeric'  # replaces item with a value with an item with a different value
print(spices)
spices.remove('allspice')  # removes item with value
print(spices)
spices.pop(3)  # removes item at index (no argument deletes last value)
print(spices)

# Tuples
# tuples are immutable (cannot be modified)
const_spices = ('garlic', 'salt', 'pepper')
print(const_spices)
