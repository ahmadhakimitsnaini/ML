"""
MODULE: OOP FUNDAMENTALS
------------------------
This script serves as a practical guide to Object-Oriented Programming (OOP) in Python.
It covers:
1. Class & Object Creation
2. Instance Attributes & Methods
3. Dunder (Magic) Methods like __init__ and __str__

Author: Ahmadhakimitsnaini
Created: 11-02-2026
"""

# ==============================================================================
# PART 1: DEFINING A CLASS (The Blueprint)
# ==============================================================================

class Employee:
    """
    A class representing an employee in an organization.
    
    Concepts covered:
    - Encapsulation: Bundling data (name, age) and methods (biodata) together.
    """

    def __init__(self, name: str, age: int, university: str):
        """
        The Constructor Method.
        Initializes the object's attributes when a new instance is created.
        
        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            university (str): Where the employee studied.
        """
        self.name = name          # Instance attribute
        self.age = age            # Instance attribute
        self.university = university # Instance attribute

    def get_biodata(self) -> str:
        """Returns a formatted string of the employee's basic info."""
        return f"{self.name} is {self.age} years old and studied at {self.university}."
    
    def show_talent(self, talent: str) -> str:
        """
        Demonstrates a method that accepts an external argument ('talent').
        """
        return f"{self.name} has a hidden talent: {talent}."


# --- Execution Example 1 ---
print("\n--- EMPLOYEE CLASS DEMO ---")

# Instantiation: Creating an object (employee1) from the class (Employee)
employee1 = Employee("Ahmadhakimitsnaini", 20, "Politeknik Negeri Madiun")

# Accessing methods
print(employee1.get_biodata())
print(employee1.show_talent("Python Coding"))


# ==============================================================================
# PART 2: DUNDER METHODS (Magic Methods)
# ==============================================================================

class Car:
    """
    A class to demonstrate special 'Dunder' (Double Underscore) methods.
    """

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        """
        The String Representation Method.
        
        Without this method, printing the object would look like: 
        <__main__.Car object at 0x00...>
        
        With this method, we can define a human-readable string description.
        """
        return f"Car Model: {self.name} | Color: {self.color}"

# --- Execution Example 2 ---
print("\n--- CAR CLASS DEMO (DUNDER METHODS) ---")

my_car = Car("BMW M3", "Red")

# When we call print(object), Python automatically looks for the __str__ method
print(my_car) 

# ==============================================================================
# THEORETICAL NOTES (4 PILLARS OF OOP)
# ==============================================================================
"""
KEY TAKEAWAYS:

1. ENCAPSULATION: 
   Wrapping data (variables) and methods together as a single unit (Class).
   
2. INHERITANCE: 
   Mechanism where a new class inherits properties from an existing class.
   
3. ABSTRACTION: 
   Hiding internal implementation details and showing only functionality.
   
4. POLYMORPHISM: 
   The ability of a function or object to behave in different forms.
"""