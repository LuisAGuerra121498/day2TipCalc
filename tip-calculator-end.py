#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = input("What is the total bill? ")
tip = input("What is the percentages of tip you want to give? ")
split = input("How many people to split the bill? ")

tip_p = round((int(tip) / 100),2) + 1

total = (int(bill) / int(split)) * tip_p

print(f"Each person should pay ${total:.2f}")