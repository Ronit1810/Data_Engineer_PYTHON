

#--> type() function
#--> The type() function is used to determine the data type of a variable or value.

age = 24
print(type(age))  # Output: <class 'int'>

name = "Ronit"
print(type(name))  # Output: <class 'str'>


#--> str() function
#--> The str() function is used to convert a value to a string data type.

age = 24
name = "Ronit"
#print("My name is " + age) #error: can only concatenate str (not "tuple") to str
print("My name is " + name)
print ("My age is " + str(age))  # Convert age to string before concatenation



#--> len() function
#--> The len() function is used to determine the length of a string, list, tuple, or other iterable.

text = "Hello, World!"
print(len(text))  # Output: 13



#--> count() method
#--> The count() method is used to count the number of occurrences of a substring in a string.

text = "Hello, World!"
print(text.count("l"))  # Output: 3

a = '''
My name is Ronit.
Ronit in ASE.
'''
print(a.count("Ronit")) # Output: 2



#--> replace() method
#--> The replace() method is used to replace occurrences of a substring with another substring in a string.

date = "2023-06-01"
print(date) # date in original format

new_date = date.replace("-", "/")
print(new_date)  # Output: 2023/06/01

# Example of replacing multiple characters in a string
phone = "+49 (176) 123-4567"
new_phone = phone.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(new_phone)  # Output: 00491761234567



#--> + join strings
#--> The + operator is used to concatenate (join) strings together.

first_name = "Ronit"
last_name = "Patel"

full_name = first_name + " " + last_name

print(full_name)  # Output: Ronit Patel

#--> Concatenating strings with variables
folder = "C:\\Users\\Ronit\\Documents"
file_name = "example.txt"
file_path = folder + "\\" + file_name
print(file_path)  # Output: C:\Users\Ronit\Documents\example.txt




#--> f-strings (formatted string literals)
#--> f-strings are a way to embed expressions inside string literals, using curly braces {}
first_name = "Ronit"
last_name = "Patel"
age = 24
full_name = f"My name is {first_name} {last_name} and I am {age} years old."
print(full_name)  # Output: My name is Ronit Patel and I am 24 years old.



#--> split() method
#--> The split() method is used to split a string into a list of substrings based on a specified delimiter.
time_stamp = "2023-06-01 12:30:45"
date_time = time_stamp.split(" ")
print(date_time)  # Output: ['2023-06-01', '12:30:45']
print('Date: ' + date_time[0])  # Output: Date: 2023-06-01
print('Time: ' + date_time[1])  # Output: Time: 12:30:45




#--> * String multiplication
#--> The * operator can be used to repeat a string multiple times.
text = "Hello"
repeated_text = text * 3
print(repeated_text)  # Output: HelloHelloHello



#--> Indexing and slicing strings
#--> Strings in Python are sequences of characters, and you can access individual characters using indexing and slicing.
word = "Programming"
print("First Character:", word[0]) # Output: P
print("Last Character:", word[-1]) # Output: g

text = "Python"
print("First Character:", text[0]) # Output: P
print("Last Character:", text[-1]) # Output: n
print("Slicing (0:6):", text[0:6]) # Output: Python
print("Slicing (2:5:2):", text[2:5:2]) # Output: th
print("Slicing(:4):", text[:4]) # Output: Pyth
print("Slicing(2:):", text[2:]) # Output: thon