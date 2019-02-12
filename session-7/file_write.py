# example of adding a new text.

FILENAME = "mynotes.txt"


f = open(FILENAME, 'r')


contents = f.read()
print("File: {}".format(f.name))
print("{}".format(contents))
f.close()

f = open(FILENAME, "a")

# write some information to the file
f.write("Hello I am proving to adding some text\n")

f.close()

