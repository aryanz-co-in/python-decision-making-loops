# nested/multiple if-else statement

# When you want to check multiple conditions and perform action based on the result (TRUE or FALSE).

x = 80
y = 10
z = 90

# Multiple if

if x > y:
    print("X is greater")
elif x > z:
    print("X is greater")
elif y > z:
    print("Y is greater")
else:
    print("Z is greater")

# Nested If

if x > y:
    if x > z:
        print("x is greater")
    else:
        print("z is greater")
elif y > z:
    print("y is greater")
else:
    print("z is greater")

print("Program Ended")



