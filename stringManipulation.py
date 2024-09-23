# upper
sentence="Hi, My name is Rajat."
upperCase=sentence.upper()
print(upperCase)

# lower
lowerCase=sentence.lower()
print(lowerCase)

# replace
name="Rajat Singh"
new_LastName="Sharma"
new_Name=name.replace("Singh",new_LastName)
print(new_Name)

# find:- returns the starting index of that str
    #if nothing found returns -1;
name="Ronni Coleman"
starting_index=name.find('z')
print(starting_index)

# split:- splits the string at the specified operator
intro="Ronnie Coleman is a legend."
split_string=intro.split(" ");
print(split_string)