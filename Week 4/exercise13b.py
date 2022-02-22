# open file as read doc
with open('pelican.txt', 'r') as pelican_doc:
# read entire contents of file 'slurp'
    text_data = pelican_doc.read()
    print(text_data)
# use split to create a new list - each line is an element
    pelican_list = text_data.split(',')
# type and length of list
    print(type(pelican_list))
    print(len(pelican_list))
# list comprehension/ for loop to print each line of the list.
# Use .strip() to remove blank lines
    for line in pelican_list:
        print(line.strip())


