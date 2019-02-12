#example of reding a file located
# in our local system

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')
#myfile is an object

# Print the filename
print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

