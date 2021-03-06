print("Welcome to the tip calc")
total_bil = input("What was the total bill? ")
tip_percentage = input("How much percent would you like to tip? ")
number_of_people = input("How many people to split the bill? ")

pay_amount = ((int(total_bil) + (int(tip_percentage) / 100 ) * int(total_bil)) / int(number_of_people))
print(pay_amount)