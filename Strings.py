name="Rajat Singh"

#1. Indexing

# Normal indexing is from 0 to len-1
print(name[0])
print(name[len(name)-1])

# Negtive Indexinf is from -len to -1;
# nagtive indexing starts from the very
# end of the string.
print(f"{name[-1]},{name[-2]},{name[-3]},{name[-4]},{name[-5]},{name[-6]},{name[-7]},{name[-8]},{name[-9]},{name[-10]},{name[-11]}")

#2. Slicing
print(name[0:3])
print(name[8:10])

#3. Stride
#We can also input a stride value as follows, with the '2' indicating that we are selecting every second variable:
print(name[::2])

#4. String Concatenation
first_name='Rajat'
last_name='Singh'
full_name=first_name+" "+last_name
print(full_name)

#5. String Replication
print(3*first_name)