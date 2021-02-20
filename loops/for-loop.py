# For loop
# it has the ability to iterate over the items of any sequence,
# such as a list or a string.

# We can iterate Collection items
# Such as List, Tuple, Set and so on.
blog_websites = ["aryanz.co.in", "balamt.in", "wecancode.live"]

for blog_site in blog_websites:
    print(blog_site)



# We can iterate String
name = "John"
for letter in name:
    print(letter)


# Using else in For loop

for i in range(1,4):
    print(i)
else:
    print(f"Reached the max range")