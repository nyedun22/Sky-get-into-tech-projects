Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# print line of hyphens same length of str
print("-" * len(Belgium))

# replace commas with colons
print(Belgium.replace(',', ':'))

# population calculation
belgium_list = Belgium.split(",")
print(belgium_list)
belgium_pop = int(belgium_list[1])
brussels_pop = int(belgium_list[3])

print(int(belgium_list[1] + belgium_list[3]))
print(belgium_pop + brussels_pop)

# dictionary





