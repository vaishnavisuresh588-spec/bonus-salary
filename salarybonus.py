import sys

# Check if salary is provided as a command-line argument
if len(sys.argv) == 2:
    # Get salary from command line
    salary = float(sys.argv[1])
else:
    # Default salary if not provided
    salary = 50000
    print("No salary provided. Using default salary of ₹50,000.\n")

# Calculate 10% bonus
bonus = 0.10 * salary
total_salary = salary + bonus

# Display results
print(f"Employee Salary:{salary:.2f}")
print(f"Bonus Amount:{bonus:.2f}")
print(f"Total Salary after Bonus:{total_salary:.2f}")
