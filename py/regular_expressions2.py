import re


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")


test_phrase = "sdsd..sssddd..sddsddd....dsds"
exclude_phrase = "This is a string! But it has a punctuation. How can we remove it?"
# '*': 0 or more
# '+': one or more
# '?': 0 or 1
# '{number}': specific number counts
# '{number1, number2}': number1 times or number2 times
test_patterns = ["sd*"]


# '[^~~]+': remove all the symbols next to '^'
# '[a-z]+': return all the lowercases letters
exclude_patterns = ["[^!.?]+"]

multi_re_find(test_patterns, test_phrase)
multi_re_find(exclude_patterns, exclude_phrase)
