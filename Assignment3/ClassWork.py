def main():
    #method1()
    #method2()
    #even_odd()
    even_odd2()
    
def method1():
    temp = 51
    if temp >= 80:
        print("I cant play golf today")
        print("Its to ", end="")
        print("Hot")
    elif temp <= 79:
        if temp < 55:
            print("Get me a coat")
            print("Its to darn ", end="")
            print("Cold")
        else:
            print("Its perfect for golf!")
            
def method2():
    name1 = "Greg"
    name2 = "GREG"
    print(name1 == name2)
    name1 = "greg"
    print(name1 == name2)
    print(name1.upper() == name2.upper())
    
def even_odd():
    user_input = int(input("Enter the value: "))
    print(f' {user_input} is ', end='')
    if user_input % 2 == 0:
        print('even')
    else:
        print('false')
        
def even_odd2():
    user_input = int(input("enter a number: "))
    print(f'{user_input} is ', end='')
    print('even' if user_input % 2 == 0 else 'odd')
main()