import math


def degree_table():
    print("Celsius\t Fahrenheit")
    print("-------------------")
    
    for celsius in range (0, 33):
        fahrenheit = (9/5 * celsius) + 32
        print(celsius, "\t", format (fahrenheit, ".1f"))
#degree_table()

def chess(square):
    grains = math.pow(2, square)
    bushel = grains / 1305000
    price = bushel * 12.17
    return(grains, bushel, price)

def chess_calculations():
    for square in range(64):
        total_grains = total_bushel = total_price = sum_grains = 0
        return_value = chess(square)
        square_grains = return_value[0]
        square_bushels = return_value[1]
        square_price = return_value[2]
        total_grains += square_grains
        total_bushel += square_bushels
        total_price += square_price
    
    print(f'{square_grains} {square_bushels} {square_price}')
    print(f'Grand totals: {total_grains} Total bushels: {total_bushel} Total price ${total_price}')
chess_calculations()

def ocean_level():
    print("Year\t Number of millimeters")
    print("----------------------------") 
    
    for year in range(1, 26): 
        num_of_millimeters = year * 1.6
        print(year, "\t", format(num_of_millimeters, ".1f"))
#ocean_level()

def factorial():
    num = int(input("Enter a number to be factored "))
    
    factorial = 1
    
    if num < 0:
        print("Number must be a positive number")
    elif num == 0:
        print("You choose zero as your number")
    else:
        for num in range (1, num + 1):
            factorial *=  num
            print("The factorial of", num, "is", factorial)
#factorial()