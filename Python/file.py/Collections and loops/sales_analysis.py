print()
print('HERE IS THE AZUBI STORE ANALYSIS ON DATA WITH THE SPECIFIED CRITERIA. \n_____________________________________________________________________________')
print()

products = ['Sankofa Foods', 'Jamestown Coffee', 'Bioko Chocolate', 'Blue Skies Ice Cream', 'Fair Afric Chocolate', 'Kawa Moka Coffee', 'Aphro Spirit', 'Mensado Blassap', 'Voltic']
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9] # number of customers that patronized each product the previous week

# CALCULATE THE TOTAL PRICE AVERAGE FOR ALL PRODUCTS.
total_price = sum(prices) # calculates the total price of all products
num_products = len(products) # calculates the number of all products
total_price_average = total_price/num_products # calculates total price average

print(f"The total price average for all products is {'GH₵ {:,.2f}'.format(total_price_average)}")
print()

# CREATE A NEW PRICE LIST THAT REDUCES THE OLD PRICES BY 5 CEDIS.
newprice_list = [] # creates a new empty list
for i in prices:
    newprice_list.append(i - 5)
    # calculates the new prices of the products and inserts them into the new empty list

print(f'The new price list that reduces the old prices by 5 cedis is : \n{newprice_list}')
print()

# CALCULATE THE TOTAL REVENUE GENERATED FROM THE PRODUCTS.
product_revenue_list = [] # creates a new empty list
for i in range(0, len(prices)):
    product_revenue_list.append(prices[i]*last_week[i])
    # calculates the revenue of each product generated and inserts them into the new empty list

total_revenue = sum(product_revenue_list) # calculates the total revenue generated from sale of the products
print(f"The total revenue generated from the products is {'GH₵ {:,.2f}'.format(total_revenue)}")
print()

# BASED ON THE NEW PRICES, WHICH PRODUCTS ARE LESS THAN 30 CEDIS.
productsandprices_dict = {} # creates a new empty dictionary
for i in range(0,len(products)):
    productsandprices_dict[products[i]] = newprice_list[i]
    # inserts the products as keys and their corresponding prices as values into the new empty dictionary

productsaskeys_list = [key for key, value in productsandprices_dict.items() if value < 30]
# gets the products whose new prices are less than 30 cedis and they are inserted into the list(productsaskeys_list)
pricesasvalues_list = [value for key, value in productsandprices_dict.items() if value < 30]
# gets the new prices which are less than 30 cedis and they are inserted into the list(pricesasvalues_list)
lessthan30_dict = {} # creates a new empty dictionary

for i in range(0,len(productsaskeys_list)):
    lessthan30_dict[productsaskeys_list[i]] = pricesasvalues_list[i]
    # inserts the products as keys and their corresponding prices as values for those products whose prices are less than 30 cedis into the new empty dictionary

print(f'The Dictionary of products and their corresponding new prices which are less than 30 cedis is : \n{lessthan30_dict}')
print()

print('Based on the new prices, the products with prices less than 30 cedis are : ')
for i in productsaskeys_list:
    print(i) # gives an output of the products whose prices are less than 30 cedis

print(' \n_______________________________________________________________________________________________________________________ \n')