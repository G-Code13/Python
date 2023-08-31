import math


def odd_Even():
    number = int(input("Enter any number: "))
    
    if number % 3:
        print("This number is even")
    else:
        print("This number is not even!")
odd_Even()

def day_Of_Week():
    day_Of_Week = int(input("Enter a number from 1 - 7 to pick which day of the week you want to start on: "))
    
    if day_Of_Week == 1:
        print("\nMonday")
    elif day_Of_Week == 2:
        print("\nTuesday")
    elif day_Of_Week == 3:
        print("\nWednesday")
    elif day_Of_Week == 4:
        print("\nThursday")
    elif day_Of_Week == 5:
        print("\nFriday")
    elif day_Of_Week == 6:
        print("\nSaturday")
    elif day_Of_Week == 7:
        print("\nSunday")
    else:
        print("\nAin't nobody got time for that, enter a valid number between 1 and 7")
day_Of_Week()

def length_Width():
    length = float(input("Enter the length of the first rectangle: "))
    width = float(input("Enter the width of the first rectangle: "))
    area1 = length * width
    print("Rectangle area 1 =%.4f" % area1)
    diagonal1 = math.sqrt(math.pow(width, 2) + math.pow(length, 2))
    print("Diagonal length %.4f" % diagonal1)
    print(" ")
    
    length = float(input("Enter the length of the second rectangle: "))
    width = float(input("Enter the width of the second rectangle: "))
    area2 = length * width
    print("Rectangle area 2 =%.4f" % area2)
    diagonal2 = math.sqrt(math.pow(width, 2) + math.pow(length, 2))
    print("Diagonal length %.4f" % diagonal2)
    print()
    
    if area1 > area2 and diagonal1 > diagonal2:
        print("Rectangle 1 area is bigger %.4f" % area1)
        print("Rectangle 1 is bigger diagonal %.4f" % diagonal1)
    elif area1 < area2 and diagonal1 < diagonal2:
        print("Rectangle 2 area is bigger %.4f" % area2)
        print("Rectangle 2 is bigger diagonal %.4f" % diagonal2)
    else:
        print("Both rectangles have the same area", "Rectangle 1 =", area1, "Rectangle 2 =", area2, "and the same diagonal", "Rectangle 1 =%.4f" % diagonal1, "Rectangle 2 =%.4f" % diagonal2)
length_Width()

def party():
    pack_Of_Ten_Hotdogs = 3.49
    pack_Of_Eight_Buns = 2.59
    package_Size_Hotdogs = 10
    package_Size_Buns = 8
    bud = 5.98
    people_Attending = int(input("Enter the number of people attending: "))
    hotdogs_Each_Person = int(input("Enter the number of hotdogs for each person: "))
    print()
    
    hotdogs_needed = people_Attending * hotdogs_Each_Person
    
    total_hotdog_packs = -1 * (-hotdogs_needed // package_Size_Hotdogs)
    print("Total hotdog packs = ", (total_hotdog_packs))
    print("Total cost for the hotdogs =", total_hotdog_packs * pack_Of_Ten_Hotdogs)
    print()
    
    total_bun_packs = -1 * (-hotdogs_needed // package_Size_Buns)
    print("Total packs of buns = ", (total_bun_packs))
    print("Total cost for hotdog buns =%.2f" % (total_bun_packs * pack_Of_Eight_Buns))
    print()
    
    leftover_hotdogs =  hotdogs_needed % package_Size_Hotdogs
    print("Leftover hotdogs =", leftover_hotdogs)
    print()

    leftover_buns = hotdogs_needed % package_Size_Buns
    print("Leftover buns =", leftover_buns)
    print()
    
    final_total = (total_bun_packs * pack_Of_Eight_Buns) + (total_hotdog_packs * pack_Of_Ten_Hotdogs) + bud
    print(f"Final total: {final_total}")
party()