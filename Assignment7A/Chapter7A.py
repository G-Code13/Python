def main():
    object_file = open('Assignment7A/accountsA/charge_accounts.txt', 'r')
    accounts_list = read(object_file)
    check(accounts_list)

def read(object_file):
    
    accounts_list = []
    #index = 0
    for i in object_file:
        print(i)
        i = i.rstrip('\n')
        accounts_list.append(i)
    #print(accounts_list)
    return accounts_list

def check(accounts_list):
    number = input('Enter a account number as a seven-digit number to check if '
                   'the file has it or not: ')
    if number in accounts_list:
        print(number, 'was found in the list.')
    else:
        print(number, 'was not found in the list.')
main()