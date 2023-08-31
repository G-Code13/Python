def main():
    fat()
    carb()
    paint_job()
    falling_distance2()
    prime()
        
def fat():
    fat_grams = float(input("Enter the total of fat grams per day: "))
    calories_from_fat = fat_grams * 9
    print("Calories from fat is: ", format(calories_from_fat, ".2f"))
    
def carb():   
    carb_grams = float(input("Enter the total of carbs per day: "))
    calories_from_carbs = carb_grams * 4
    print("Calories from carbs is: ", format(calories_from_carbs, ".2f"))
    print()
    
def paint_job():
    square_feet = float(input("Enter the total square feet of wall to be painted: "))
    price_per_gallon = float(input("Enter the price for a gallon of paint: "))
    gallons_of_paint = square_feet / 112
    labor = gallons_of_paint * 8
    paint_cost = gallons_of_paint * price_per_gallon
    total_cost = labor * paint_cost
    print("Gallons of paint needed: ", gallons_of_paint, "Labor cost: ", labor, "Paint cost: ", paint_cost)
    print("Final Total", total_cost)
    print()
    
def falling_distance(falling_time):
    gravity = 9.8
    distance = (1/2) * gravity * (falling_time **2)
    return distance

def falling_distance2():
    print("Time(s)\t   Distance Fallen(m)")
    print("----------------------------")
    for seconds in range (1, 11):
        distance_fallen = falling_distance(seconds)
        print(format(seconds, "4.0f"), format(distance_fallen, "17.2f"))
        print()
    
def prime():
    number = int(input("Enter a number between 1 and 10000: "))
    if number == 0:
        print("Please pick a positive number!")
    elif number == 1:
        print(" 1 is not a prime number = false")
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number = false")
                break
            else:
                print(number, "is a prime number = true")
                break
    print()
main()
