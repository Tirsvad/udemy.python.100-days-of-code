# If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculater!")
# Each person should pay (150.00 / 5) * 1.12 = 33.6
bill = float(input("What is the bill ? $ "))
# Format the result to 2 decimal places = 33.60
tip = int(input("how much tip would you like to give? 10, 12, or 15? ")) / 100
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people = int(input("How many people to split the bill? "))
# Write your code below this line 👇
bill_with_tip = round((bill + bill * tip) / people, 2)
bill_final = "{:.2f}".format(bill_with_tip)

# Both give the same result
print(f"The bill is ${bill_with_tip}")
print(f"Each person should pay: ${bill_final}")
