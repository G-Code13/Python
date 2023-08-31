def main():
    object_file = open('Assignment7A/accountsA/charge_accounts.txt', 'r')
    accounts_list = read(object_file)
    check(accounts_list)#returns from method
    
    boyNames = open('Assignment7A/boyNames/BoyNames.txt', 'r')
    bNames = read(boyNames)
    getNames(bNames)
    
    girlNames = open('Assignment7A/girlNames/GirlNames.txt', 'r')
    gNames = read(girlNames)
    getNames(gNames)
    
    population = open('Assignment7A/population/USPopulation.txt', 'r')
    isPopulation = read(population)
    population_totals(isPopulation)

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
        print(number, ' was found in the popular name list.')
    else:
        print(number, ' was not found in the popular name list.')
#--------------------------------------------------------------------       
def nameFinder1(boyNames):
    bNames = []
    for i in boyNames:
       print(i)
       i = i.rstrip('\n')
       bNames.append(i) 
    return bNames

def getNames(bNames):
    name = input('Enter a name to find: ')
    if name in bNames:
        print(name, ' was found in the popular name list.')
    else:
        print(name, ' was not found in the popular name list.')

def nameFinder1(girlNames):
    gNames = []
    for i in girlNames:
       print(i)
       i = i.rstrip('\n')
       gNames.append(i) 
    return gNames

def getNames(gNames):
    name = input('Enter a name to find: ')
    if name in gNames:
        print(name, ' name found')
    else:
        print(name, ' name not found')
#-----------------------------------------------------------------------
def population_data(population):
    isPopulation = []
    for i in population:
        print(i)
        i = i.rstrip('\n')
        isPopulation.append(i)
    return isPopulation
 
def population_totals(isPopulation):   
    sum_total = 0.0
    average = 0.0
    
    for value in isPopulation:
        sum_total += int(value)
        average = sum_total / (len(isPopulation))
    print('AVERAGE population between 1950 -1990 is ','%.5f' % average)
    
    max_population = max(isPopulation)
    index = isPopulation.index(max_population)
    year = 1950 + index
    print('Total', max_population, 'Max population in year', year)
    
    min_population = min(isPopulation)
    index = isPopulation.index(min_population)
    year = 1950 + index
    print('Total', min_population, 'Min population in year', year)
if __name__ == "__main__":
    main()