def Add(x, y):
    return x + y

def Fahrenheit_To_Centigrade(celsius):
    return (celsius * 9/5) + 32

def Factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def Divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if isinstance(y, str):
        raise TypeError("Divisor must be a number, not a string")
    return x / y

def Even(num):
    return num > 0