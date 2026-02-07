# LEARN ALL ABOUT FUNCTION 

# --- 1. LAMBDA FUNCTIONS (Syntax = lambda arguments : expression) ---

# Example from lambda function
x = lambda y : y + 10       # Lambda with single parameter
z = lambda x, y : x * y     # Lambda with multi parameter


                            
def myFunc(x) :              # The power of lambda is better shown when you -
    return lambda y : y * x  # use them as an anonymous function inside another function.

nextFunc = myFunc(5)
print(nextFunc(10))

# --- 2. LAMBDA FUNCTION WITH BUILT-IN FUNCTIONS ---

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]                 # Make a List For Example
some = ["Apple", "Banana", "Mango", "Strawberry"]    # Make a List in String

# 1. Using Lambda with map()
doubled = list(map(lambda x : x * 2, number))        # This function Will doubled a number on the list.
print(doubled)    

# 2. Using Lambda with filter()
ganjil = list(filter(lambda y : y % 2 != 0, number)) # This function Will filter which number can divided by 2
print(ganjil)

# 3. Using Lambda with sorted()
words = sorted(some, key = lambda x : len(x))        # This Function Will Sorted a List by String
print(words)



