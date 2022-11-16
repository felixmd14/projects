num = int(input('Please enter a number: '))
def factorial(n):
    result = 1
    
    if n > 1:
        for i in range(1, n+1):
            result *= i

    return result

print(f'{num} factorial is: {factorial(num)}')