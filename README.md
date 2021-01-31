Python Decision making and Loops
-------------------------------------------

# Decision Making
It is also known as Control flow, lets us see the below list of decision-making statements

Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome. 
You need to determine which action to take and which statements to execute if outcome is TRUE or FALSE otherwise.

1. if statement
2. if-else statement
3. nested if statement

```
                                  [O]
                                   |
                                   |
                                   V
                                 // \
                               //     \
                              //  IF   \
                             //Condition\ ___________
                             \          /           |
                              \        /            |
                                \     /             |
                                 \   /              |
                                   ||                |
                                   ||                V
         if condition is True      ||                | if condition is 
                                   ||                |  False
                         ---------------------       |
                         |      Some Code    |       |
                         |___________________|       |
                                   ||                |
                                   ||                |
                                   ||                |
                                   ||<---------------|
                                   ||
                                   ||
                                    V
                                   (O)
                                    

```



```
Note: Python programming language assumes any non-zero and non-null values as TRUE, and if it is either zero or null, then it is assumed as FALSE value
```

# Loops
A loop statement allows us to execute a statement or group of statements multiple times.

1. while loop
2. for loop
3. nested loop

Apart from the above loops, we have 3 statements used in Looping
1. break
2. continue
3. pass

```
                                  [O]
                                   |
                                   |
                                   |------<----------|
                                   |                 |
                                   |                 |
                                   |                 |
                                   |                 |
                                   |        |---------------------|
                                   |        |       Some Code     |
                                   |        |_____________________|
                                   |                 |
                                   |                 |
                                   |                 |                                           
                                  / \               ^  When Condition
                                 /    \             |   is TRUE, Go in Loops
                                /       \           |   Until Condition is FALSE.
                               /Condition \_________|
                               \           /
                                \         /
                                 \      /
                                   \   /
                                    \ /
                                     ||
                                     ||
                                     || When Condition is FALSE
                                     ||
                                   (EXIT)

```





