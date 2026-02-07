# LEARN ALL ABOUT FUNCTION 

# 1. LAMBDA FUNCTIONS (Syntax = lambda arguments : expression)

# Example from lambda function
x = lambda y : y + 10       # Lambda with single parameter
z = lambda x, y : x * y     # Lambda with multi parameter


# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myFunc(x) : 
    return lambda y : y * x

nextFunc = myFunc(5)
print(nextFunc(10))

# 2. LAMBDA FUNCTION WITH BUILT-IN FUNCTIONS

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# 1. Using Lambda with map()
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled = list(map(lambda x : x * 2, number))  # This function will doubled a number on the list.
print(doubled)    

# 2. 




