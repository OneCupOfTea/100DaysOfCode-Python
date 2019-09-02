import random

num1= 2        # int : positive or negative numbers, without decimals, of unlimited length.
num2= 3.4      # float : positive or negative numbers with containing one ormore decimals.
num3= 13e4     # float can also be scientific numbers with an "e" to indicate the power of 10
num4= 5j       # complex : are positive or negative numbers, written with a "j" as the imaginary part
num5= 6+4j
# We use type() function to print the datatype of a variable
print("num1 of type: ",type(num1))
print("num2 of type: ",type(num2))
print("num3 of type: ",type(num3))
print("num4 of type: ",type(num4))
print("num5 of type: ",type(num5))

# Type Conversion
#convert from int to float
n1= 4
f1= float(n1)
print(f1)
print(type(f1))
#convert from float to int
f2= 5.0
n2= int(f2)
print(n2)
print(type(n2))
#convert from int to complex,    complex numbers can't be converted to other types of numbers
n3= 1
c3= complex(n3)
print(c3)
print(type(c3))

# Random numbers
print("random number: ",random.randrange(1,5))