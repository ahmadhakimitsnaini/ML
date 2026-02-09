# LEARN ALL ABOUT FUNCTION 

# --- 1. LAMBDA FUNCTIONS (Syntax = lambda arguments : expression) ---

# Example from lambda function
x = lambda y : y + 10        # Lambda with single parameter
z = lambda x, y : x * y      # Lambda with multi parameter


                            
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


# --- 3. RECURSION FUNCTIONS (Recursion is when a function calls itself. is a common mathematical and programming concept) ---

# Example for Recursion Functions
def countdown (n) : 
    if n <= 0 :
        print("Done")
    else : 
        print(n)
        countdown(n - 1)              # This statement will call function it self.

# Base Case and Recursive Case
def factorial(n) : 
    if n == 1 or n == 0 :             # A base case - A condition that stops the recursion.
        return 1 
    else : 
        return n * factorial(n - 1)   # A recursive case - The function calling itself with a modified argument.
                                      # Without base case will make function call it self forever, and causing stack overflow error.
print(factorial(5))                     

# Fibonacci Sequence Rumus = F(n) = F(n−1) + F(n−2)  
def fibonacci(n) : 
    if n <= 1 :                       # This important to stop recursion
        return n
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))                  # This mean is fibonacci(6) = 8 + fibonacci(5) = 5.
    

# --- 4. Recursion with Lists (Recursion can be used to process lists by handling one element at a time) ---

# Calculate the sum of all elements in a list:
def sumList(numbers) : 
    if len(numbers) == 0 :
        return 0
    else : 
        return numbers[0] + sumList(numbers[1:])  # Sum all element on list

sumNumList = [1, 2, 3, 4, 5]
print(sumList(sumNumList))

# Find the maximum value in a list:
def find_max(max) : 
    if len(max) == 1 :                                          # Base Case
        return max[0]
    else : 
        check_max = find_max(max[1:])                           # Take list from first index until last index and remove first element.
        return max[0] if max[0] > check_max else check_max      # compare the first element with rest of list.

maximal = [1, 2, 3, 4, 5, 6, 7, 8]
print(find_max(maximal))

# Find the minimum value in a list
def find_minim(minim) :
    if len(minim) == 1:
        return minim[0]
    else : 
        check_minim = find_minim(minim[1:])
        return minim[0] if minim[0] < check_minim else check_minim
    
minimal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_minim(minimal))


