# Program that calculates the total amount of a meal purchased with a fixed tip.
# Should ask the user to enter the charge for the food.
# Calculate the amounts of an 18 percent tip and 7 percent sales tax.
# Display each of these amounts and the total.
# Generate script that meets the requirements.

food_charge = float(input('Enter the charge for the food: GH₵ ')) #user enters the charge for the food
tip = (18/100)*food_charge # tip = 18% of charge for food
sales_tax =(7/100)*food_charge # sales tax = 7% of charge for food
Total = food_charge +tip + sales_tax
print(f"Tip = {'GH₵ {:,.2f}'.format(tip)} \nSales tax = {'GH₵ {:,.2f}'.format(sales_tax)} \nGrand Total = {'GH₵ {:,.2f}'.format(Total)}" )