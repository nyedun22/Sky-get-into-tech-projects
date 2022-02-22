# import sys module
import sys
# variable measures number of arguments
count_of_arguments = len(sys.argv)
if count_of_arguments > 1:
    print('Too many args')
    print('arg 1 is ' + sys.argv[1])
    print('arg 2 is ' + sys.argv[2])
else:
    where = 'World'
    print("Hello", where)
# prints import from file path
print('Goodbye from ' + sys.argv[0])

#(venv) natashaedun@Natashas-MacBook-Pro PythonWeek1 % python /Users/natashaedun/Documents/PythonWeek1/anatomy.py natasha pasta
# in terminal