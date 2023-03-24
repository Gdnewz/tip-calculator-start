#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What is your total bill? ")

percent = input("What percentage tip would you like to give? 10, 12 or 15?")

split = input("How many people to split the bill? ")

bill_change = float(bill)
percent_as_int = int(percent)

new_percent = bill_change * (percent_as_int / 100)

split_as_int = int(split)
new_bill = new_percent + bill_change
amount_to_pay = (new_bill / split_as_int)
amount_to_pay = round(amount_to_pay, 2)
print(f"Each person should pay: {amount_to_pay} ")
