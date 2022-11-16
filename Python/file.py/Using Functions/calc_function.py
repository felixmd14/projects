def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtraction,
    '*' : multi,
    '/' : div

}
print('The operation symbols available are:')

def calculator():
    for symbol in operations:
        print(symbol, end = ' ')
    print()

    should_continue = True
    while should_continue:
        print()
        num1 = float(input('Enter the first number: '))
        operation_symbol = input('Enter the symbol: ')
        num2 = float(input('Enter the second number: '))

        calculated_value = operations[operation_symbol]

        answer = calculated_value(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

calculator()