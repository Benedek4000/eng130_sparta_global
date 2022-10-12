story1 = {
    'start': 'The mysterious hero travels to the dragon`s den.',
    'middle': 'The mysterious hero slays the dragon and saves the princess.',
    'end': 'The mysterious hero and the princess go clubbing.'
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
for key in story1.keys():
    print(story1[key])
story1['hero'] = 'Ebay Shrek'