from sys import argv
script, filename = argv

prompt = ('> ')

print("What word would you like to be replace?")
word = input(prompt)
# Read in the file
with open(filename, 'r+') as file :
  filedata = file.read()

print("What word would you like to input?")
new = input(prompt)

# Replace the target string
filedata = filedata.replace(word, new)

# Write the file out again
with open(filename, 'w') as file:
  file.write(filedata)
