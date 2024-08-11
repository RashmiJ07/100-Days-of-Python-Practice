#Day 2 | Tip Calculator
# This program calculates the tip amount and the final amount each person needs to pay.

print("Welcome to the Tip Calculator!")

# Get user inputs
bill_amount = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people_to_split_with = int(input("How many people to split the bill with? "))

# Calculate the tip amount
tip_amount = (bill_amount * tip_percentage) / 100.0

# Calculate the final bill amount
final_bill_amount = bill_amount + tip_amount

# Calculate the amount each person should pay
per_person_split = final_bill_amount / total_people_to_split_with

# Display the result
print(f"Each person should pay: ${per_person_split:.2f}")
