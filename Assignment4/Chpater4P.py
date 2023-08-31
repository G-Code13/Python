import math


def main():
    # num()
    # num2()
    # num3()
    # num4()
    #num5()
    juggler()
    #juggler2()
    
def num():
    for numbers in range(1, 11):
        print(numbers, end=' ')
    print()

def num2():
    for numbers in range(100, 5, -5):
        print(numbers, end=' ')
    print()
    
def num3():
    for numbers in range(10, 16):
        for exponent in range(1, 6):
            print(f'{numbers} ^ {exponent} = {numbers * exponent}')
    print()

def num4():
    for number in range(1, 21):
        print(f'{number} squared {num **2}')
    print()   
    
def num5():
    counter = 0
    totalValue = 0
    
    while(True):
        tempValue = int(input("Enter a positive number, -99 to quit "))
        if tempValue == -99:
            if counter != 0:
                print(f'Average is {totalValue/counter}')
            else:
                print("No average to calculate")
            break
        totalValue += tempValue
        counter += 1

def juggler():
        
    print("Jugglers")
    counter = 3 
    while counter > 1:
        print("{:,}".format(counter), end=' ')
        if counter % 2 == 0:
            factor = .5
        else:
            factor = 1.5
        counter = math.floor(counter ** factor)
    print(1)
    
#code not working
# def juggler2():
#     for i in range (1, 30):
#         juggler2(i)  
          
#     print("Jugglers")
#     counter = 3 
#     while counter > 1:
#         print("{:,}".format(counter), end=' ')
#         if counter % 2 == 0:
#             factor = .5
#         else:
#             factor = 1.5
#         counter = math.floor(counter ** factor)
#     print(1)   
if __name__ == '__main__':
    main()