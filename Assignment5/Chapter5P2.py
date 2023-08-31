def main():
    x = 15
    y = 3.14159
    
    print(f"addition ({x} {y}) = {addition(x, y)}")
    print(f"subtraction ({x} {y}) = {subtraction(x, y)}")
    print(f"multiplication ({x} {y}) = {multiplication(x, y)}")

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

if __name__ == '__main__':
    main()