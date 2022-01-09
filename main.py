print("Welcome to the tip Calculator!")

bill = float(input("What was the total bill? $"))
# print(type(bill))         #---checking the datatype of the data entered by the user
tip = int(input("How much tip would you like to give?  10, 12, or 15"))
people = int(input("How many people to split the bill? "))

tip_as_a_percent = tip / 100
total_tip_amount = bill * tip_as_a_percent

total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person,2 )            # to round the decimal places to the 2 digits
final_amount = "{:.2f}".format(bill_per_person)     #to format the decimal places to format of two

print(f"Each person should pay: ${final_amount}")
