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
# tuples are immutable lists (cannot be modified)
const_spices = ('garlic', 'salt', 'pepper', 'salt')
print(const_spices)
print(const_spices.count('salt'))  # counts the times [arguments] appears
print(const_spices.index('pepper'))  # finds the index of [argument]

# Sets
# a set is a list with no duplicates and is unordered
ingredients = {'onion', 'garlic', 'lard', 'potato', 'sausage'}
print(ingredients)
ingredients.add('salt')  # add item to set
print(ingredients)
ingredients.add('garlic')  # cannot add same item to set
print(ingredients)
ingredients.update({'rum', 'mint', 'ice', 'sugar'})  # add sets together
print(ingredients)
# other methods include: difference, intersection, union, pop, remove

# Dictionaries

