# Python Programming - www.aryanz.co.in

# Nested loop
# looping inside another loop is call nested loop

# What is the output of the following code?

for x in range(1, 5):
    for y in range(x-1, x): # 1, 4
        print(f"{y}")
    print(f"\t")
