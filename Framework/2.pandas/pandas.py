import pandas as pd

# 1. Create a simple dataset (Dictionary)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 55000, 70000]
}

# 2. Convert the dictionary into a pandas DataFrame
df = pd.read_dict(data)

# 3. Display the DataFrame
print("--- Employee Table ---")
print(df)

# 4. Basic Data Operations
print("\n--- Average Age ---")
average_age = df['Age'].mean()
print(f"The average age is: {average_age}")

print("\n--- Filter: Employees older than 25 ---")
older_employees = df[df['Age'] > 25]
print(older_employees)

print("\n--- Add a New Column (Bonus) ---")
# Let's say everyone gets a 10% bonus
df['Bonus'] = df['Salary'] * 0.10
print(df)