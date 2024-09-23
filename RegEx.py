# In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.

# This RegEx module provides several functions for working with regular expressions, including search, split, findall, and sub.

# Python provides a built-in module called re, which allows you to work with regular expressions. First, import the re module

# import re
# The search() function searches for specified patterns within a string. Here is an example that explains how to use the search() function to search for the word "Jackson" in the string "Michael Jackson is the best".

import re

# search():-finds specified pattern
strs="abc cde ropporjjaa"
pattern=r"cde"
result=re.search(pattern,strs)
if result:
    print("Found")
else:
    print("Not Found")


# Regular expressions (RegEx) are patterns used to match and manipulate strings of text. There are several special sequences in RegEx that can be used to match specific characters or patterns.

# | Special Sequence | Meaning                 | 	Example             |
# | -----------  | ----------------------- | ----------------------|
# |\d|Matches any digit character (0-9)|"123" matches "\d\d\d"|
# |\D|Matches any non-digit character|"hello" matches "\D\D\D\D\D"|
# |\w|Matches any word character (a-z, A-Z, 0-9, and _)|"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"|
# |\W|Matches any non-word character|	"@#$%" matches "\W\W\W\W"|
# |\s|Matches any whitespace character (space, tab, newline, etc.)|"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"|
# |\S|Matches any non-whitespace character|"hello_world" matches "\S\S\S\S\S\S\S\S\S"|
# |\b|Matches the boundary between a word character and a non-word character|"cat" matches "\bcat\b" in "The cat sat on the mat"|
# |\B|Matches any position that is not a word boundary|"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"|

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# fundall() function finds all occurrences of a specified pattern within a string.
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

#The sub function of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.
# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 