#dividebyzero
"""Simple Exception handling example."""
while True:
     # attempt to convert and divide values
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter Denominator:'))
        result = number1/number2
    except ValueError: # tried to convert non-numeric value to int
        print('you must enter two integers\n')
    except ZeroDivisionError: # denominator was 0
        print('Attempted to divide by zeroo,change denominator\n')
    else: # executes only if no exceptions occur
        print(f'{number1:.3f}/{number2:.3f} = {result:.3f}')
        break #terminates loop  