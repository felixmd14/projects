p = float(input('Mortgage loan principal :GHS ')) # enter the mortgage loan principal
i = float(input('Percent annual rate :'))/100/12 # enter the percent annual interest rate (i calculates percent monthly rate)
r = float(input('Years to pay off mortgage :'))*12 # enter the number of years to pay off mortgage (r calculates months to complete payment)
m = (p*(i*(1+i)**r))/(((1+i)**r)-1) # mortgage calculator
print(f"For a {int(r/12)}-year mortgage loan of {'GHS {:,.2f}'.format(p)} at an annual interest rate of {'{:,.2f}'.format(i*100*12)}%; \nyou pay: ")
print(f"{'GHS {:,.2f}'.format(m)} monthly \n_____________________ \nTotal amount paid will be {'GHS {:,.2f}'.format(m*r)}")