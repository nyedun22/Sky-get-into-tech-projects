
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

with open('pelican.txt', 'w') as pelican_doc:
   pelican_doc.write('A wonderful bird is the pelican,\n')
   pelican_doc.write('His bill holds more than his belican,\n')
   pelican_doc.writelines(lines)



