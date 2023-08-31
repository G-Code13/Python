
def main():
    accountList = open("Assignment7/accounts/charge_accounts.txt", "r")
    updated = accountList.readlines()
    check(updated)
    
def chargeAccounts(files): 
    updated = []
    
    for lines in files:
        print(lines)
        lines = lines.rstrip("\n")
        updated.append(lines)
        # if lines[-1] == "\n":
        #     updated.append(lines[:-1])
        # else:
        #     updated.append(lines)
    print(updated)
    return updated

def check(updated):   
    search = int(input("Enter the 7 digit charge account number: "))
    
    if search in updated:
        print(search, "Account was found")
    else:
        print(search, "INVALID ACCOUNT, account not found")
main()