def mpg():
    miles_Driven = input("Enter the miles driven: ")
    gallons_Of_Fuel = input("Enter the cost of fuel: ")
    miles_Driven = float(miles_Driven)
    gallons_Of_Fuel = float(gallons_Of_Fuel)
    mpg = miles_Driven / gallons_Of_Fuel
    print("Total miles per gallon = ", mpg)
mpg()

def temp():
    celsius = input("Enter the temperature in celsius: ")
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print("The temperature is", fahrenheit, "degrees outside")
temp()

def grape_Vines():
    length = int(input("Enter the length of the row in feet: "))
    end_Post = int(input("Enter the amount of space used by and end-post in feet: "))
    between_Vines = int(input("Enter the amount of space between the vines in feet: "))
    grape_Vines = length - 2 * end_Post / between_Vines
    print("Row length: ", length, end="\n")
    print("End post width: ", end_Post, end="\n")
    print("Width between vines: ", between_Vines, end="\n")
    print("Total number of grape vines: ", grape_Vines, end="\n")
grape_Vines()

def compound():
    P_Principal_Balance = float(input("Enter the initial balance: $"))
    r_Annual_Rate = float(input("Enter the interest rate: " ))
    n_Times_Per_Year = float(input("Enter how many time per year the interest is added: "))
    t_Years_In_Account = float(input("How many year(s) should it stay in the account: "))
    r_interest_Rate = r_Annual_Rate / 100
    A_Total_After_Time = P_Principal_Balance * (pow((1 + r_interest_Rate), t_Years_In_Account))
    print("Total interest gained: $%.4f" % A_Total_After_Time)
compound()