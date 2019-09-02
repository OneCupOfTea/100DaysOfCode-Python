# We can combine strings and numbers by using the format() function
# and by placing the placeholders {} in the string
age= 24
txt= "I am Najeeb, and I am {} years old"
print(txt.format(age))

name = "Najeeb"
txt= "I am {}, and I am {} years old"
print(txt.format(name, age))

# We can use index numbers [0] to be sure the arg. are placed in the correct placeholders.
txt= "I am {0}, and I am {1} years old"
print(txt.format(name, age))
