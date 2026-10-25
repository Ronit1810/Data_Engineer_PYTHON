

# type() function
# The type() function is used to determine the data type of a variable or value.

age = 24
print(type(age))  # Output: <class 'int'>

name = "Ronit"
print(type(name))  # Output: <class 'str'>


# str() function
# The str() function is used to convert a value to a string data type.

age = 24
name = "Ronit"
#print("My name is " + age) #error: can only concatenate str (not "tuple") to str
print("My name is " + name)
print ("My age is " + str(age))  # Convert age to string before concatenation