def main():
    #escape_characters()
    formatting_numbers()
    
def escape_characters():
    # Escape characters
    #     \n = new line
    #     \t = tab
    #     \' = single quote mark is printed 
    #     \" = double quote mark is printed 
    #     \\ = backslash character is printed 
    print('Mon\tTues\tWed')
    print('Thur\tFri\tSat')
    print("Your assignment is \"Hamlet\" due by tomorrow")
    print("I\'m doing great")

def formatting_numbers():
    amount_due = 5000.00
    monthly_payment = amount_due / 12
    print("Your monthly payment is: ", format(monthly_payment, ".2f"))
    
    #Inserting comma separators
main()
