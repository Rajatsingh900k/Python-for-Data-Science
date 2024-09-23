# String Formatting


#1. fstring 
full_name='Rajat Singh'
age=22
print(f'My name is {full_name} and my age is {age}')
x=10
y=10
print(f"F-strings can also be used to evaluate the expression ex: x+y={x+y}")

#2. str.format()
name='Rajat'
age=22
print('My name is {} and I am {} years old.'.format(name,age))


#3. % Operator
name='Rajat Singh'
age=22
print('My name is %s and I am %d years old.' %(name,age))


#4. Raw String(r'')
# In Python, raw strings are a powerful 
# tool for handling textual data, especially when dealing with escape characters. 
# By prefixing a string literal with the letter ‘r’, 
# Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences.

# Consider the following examples of regular string and raw string:

regular_string="C:\new_folder\file.txt"
print("Regular String:",regular_string)

# In the regular string regular_string variable, 
# the backslashes (\n) are interpreted as escape sequences. 
# Therefore, \n represents a newline character, 
# which would lead to an incorrect file path representation.

raw_string=r"C:\new_folder\file.txt"
print("Raw String:",raw_string)