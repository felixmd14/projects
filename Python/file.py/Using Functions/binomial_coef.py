def factorial(n):
    result = 1
    
    if n > 1:
        for i in range(1, n+1):
            result *= i

    return result

def binomial_coef(n, k):
    n_fac = factorial(n)
    k_fac = factorial(k)
    n_minus_k_fac = factorial(n-k)

    binomial_coef = n_fac/(k_fac*n_minus_k_fac)

    return binomial_coef
set = int(input('How many items are in the set you want to choose from: '))
choose_items = int(input('How many items will you chose from the set: '))
print(f'The number of possible combinations, rounded to the nearest whole number, of {choose_items} item(s) chosen from a set of {set} items is: {int(binomial_coef(set, choose_items))}')