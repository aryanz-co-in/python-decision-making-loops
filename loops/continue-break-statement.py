# Python Programming - www.aryanz.co.in

# Continue statement - It is used when we need to continue the code execution.
# break statement - As it name says, it will break the loop and resumes execution.

for count in range(0, 5):
    print(f"Now its {count}")
    if count == 2:
        print("count is 2, going to continue the loop")
        continue
    elif count == 3:
        print("count is 3, going to break the loop")
        break

print("Program ended")