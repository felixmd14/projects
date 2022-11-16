def is_divisible(a, b):
    '''
    Checks if a is divisible by b without a remainder
    '''
    return a % b == 0

def is_prime(n):
    '''
    Checks if n is a prime number
    '''
    for i in range(2, n):
        if is_divisible(n, i):
            return False
    return True

num = int(input('Please enter a number: '))
print(f'{num} is a prime number: {is_prime(num)}')
print()