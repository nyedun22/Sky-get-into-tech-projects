# glob module is used to retrieve files/path names matching a specified pattern
import sys, glob, os

# Get the directory name
if sys.platform == 'Win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
for file_name in glob.glob('*.py'):
    print(file_name)

# TODO: use os.path.getsize to find each file's size
for file_name in glob.glob(pattern):
    file_size = os.path.getsize(file_name)


# TODO: Add a test to only display files that are not zero length
for file_name in glob.glob(pattern):
    if file_size > 0:
        print(file_size)
        print(file_name)
        print(os.path.basename(file_name))

# print len(files) != 0:
    # print(pattern)
    # TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

