def main():
    # print(f"Even numbers in a list")
    # evenNumbers = [2, 4, 6, 8]
    # print(f"{type(evenNumbers)} {evenNumbers}")
    
    # print(f"\n List of several different data types")
    # info = ["Greg", 99, 3.14159]
    # print(f"{type(info)} {info}")
    
    # for i in range(len(info)):
    #     print(f"{type(info[i])} {info[i]}")
    
    # print(f"Create a list of 5 numbers using range command")
    # numbers = list(range(5))
    # print(f"{type(numbers)} length: {len(numbers)}{numbers}")
    
    # print(f"List using [0] * 5 \n{[0] * 5}")
    # print(f"Change first element to 15 using numbers[0] = 15")
    # numbers[0] = 15
    # print(numbers)
    
    # list1 = [1, 3, 5, 7]
    # list2 = [2, 4, 6, 8]
    # list3 = list1 + list2
    # print(f"Lets add (concatenation) two list together")
    # print(f"{list1} + {list2} = {list3}")
    # print(f"Sorted but not permanent{sorted(list3)}")#not a permanent sort
    # print(list3)
    # list3.sort()#permanent sort
    # print(f"Permanent sort {list3}")
    
    # #append a list
    # print(f"A way to create a list")
    # squares = []
    # for x in range(1,10):
    #     squares.append(x**2)
    # print(squares)
    
    # #list comprehension
    # print(f"Another way us to use ")
    # squares = [x **2 for x in range(10)]
    # print(squares)
    
    # days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # sunday = days[0]
    # friday = days[5]
    # print(f"{sunday} and {friday}")
    # midDays = days [2:5]
    # print(f"days [2:5] {midDays}")
    
    # print("\n\nMore List")
    # names = ["Angela", "Richard", "Razanne", "Eric",
    #          "Jacob", "Jonathan", "Sergio", "Felicity", "Issac",
    #          "Janet", "Gregory", "Griffon"]
    
    # search = "Razanne"
    # if search in names:
    #     print(search, " was found")
    # else:
    #     print(search, "was not found")
        
    # names.append("Matthew")
    # names.append("Mark")
    # names.append("Luke")
    # print(names)
    
    # # names.insert("John")
    # # names.insert("Paul")
    # # names.insert("George")
    # # names.insert("Ringo")
    # # print(names)
    
    # names.sort()
    # print(names)
    
    # # names.remove("Paul")
    # # print(names)
    # # names.reverse()
    # # print(names)
    
    # print(f"min value of names: {min(names)}")
    # print(f"min value of names: {max(names)}")
    # print()
    
    # #this does not create a new list or copy
    # names2 = names
    # print(names2)
    # print()
    # names2.reverse
    # print(f"1 {names}")
    # print(f"2 {names2}")
    
    # names2 = []
    # for item in names:
    #     names2.append(item)
    # names2.reverse()
    # print(f"1 {names}")
    # print(f"2 {names2}")
    # print()
    
    # print(f'name.pop() = {names.pop()}') #removes the last item
    # print(f'name.pop() = {names.pop(5)}') #removes the 5th item
    # print()
    # print()
    

    print("\nTwo dimensional")
    calories = [[ 'Sunday', 500, 800, 900],
                [ 'Monday', 550, 850, 950],
                [ 'Tuesday', 600, 900, 1000],
                [ 'Wednesday', 650, 950, 1050],
                [ 'Thursday', 450, 750, 850],
                [ 'Friday', 400, 700, 800],
                [ 'Saturday', 350, 800, 1100]]

    for day in range(len(calories)):
        for meal in range(len(calories[day])):
            print(calories[day][meal], end=' ')
        print()
if __name__ == "__main__":
    main()