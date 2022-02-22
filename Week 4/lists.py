cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# initial code adds each letter separately to the list
# += adds items as a sequence which is why characters are added individually
cheese.append('Oke')
print(cheese)

# use extend to add multiple items to list within single line of code
more_cheese = ["Mozzerella", "Brie"]
cheese.extend(more_cheese)
print(cheese)