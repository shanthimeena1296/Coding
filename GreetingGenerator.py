'''
This will generate greeting based on the name provided!
In this implementation, the greeting_gen function takes an optional argument name, which defaults to None.
If name is provided, the function returns a string that says "Hello, NAME!", where NAME is the value of the name argument. 
If name is not provided, the function returns a string that says "Hello there!".
'''

def greeting_gen(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, there!"

print(greeting_gen("shanthi"))