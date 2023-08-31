def main():
    emptySet = set()
    mySet = set(["three", "two", "one"])#tuples ([])
    print(mySet)
    
    mySet1 = set([1, 2, 3, 4, 5, 6])
    mySet2 = set([95, 96, 97, 98, 99])
    
    print(len(mySet1))
    for returnValue in mySet1:
        print(returnValue, end=' ')
    print()
    
    mySet1.add(7)
    mySet2.add(94)
    for value in mySet2:
        print(value, end=' ')
        
    
if __name__ == "__main__":
    main()