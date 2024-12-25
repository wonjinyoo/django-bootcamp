# REGULAR EXPRESSIONS

import re

patterns = ["term1", "term2"]

text = "This is a string with term1"

for pattern in patterns:
    print("I am searching for: " + pattern)

    # Finding if a pattern is inside "text":
    if re.search(pattern, text):
        print("MATCH!")
    else:
        print("NO MATCH")


match = re.search("term1", text)

# Finding "index" where the match starts/ends:
print(match.start())
print(match.end())


# Splitting string:
split_term = "@"
email = "user@gmail.com"
print(re.split(split_term, email))


# Returning a list of all-overlapping matching string:
print(re.findall("match", "test phrase match match in middle"))
