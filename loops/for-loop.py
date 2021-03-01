# For loop
# it has the ability to iterate over the items of any sequence,
# such as a list or a string.

# We can iterate Collection items
# Such as List, Tuple, Set and so on.

# Example 1 : looping list
blog_websites = ["aryanz.co.in", "balamt.in", "wecancode.live"]

for x in blog_websites:
    print(x)


# Example 2 : looping string value
name = "John"
for letter in name:
    print(letter)


# Example 3: Using else in For loop

for i in range(1,4):
    print(i)
else:
    print(f"Reached the max range")
