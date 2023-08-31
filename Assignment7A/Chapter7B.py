def main():
    print("\n\nTuples")
    tuple1 = (1, 3, 5, 7,)
    print(f"type(tuple1) {type(tuple1)}")
    print(f"len(tuple1) {len(tuple1)}")
    for x in range(len(tuple1)):
        print(f"{x} {tuple1}")
        
    length = len(tuple1)
    print(f"{tuple1[0:length]}")
    
    print(f"{len(tuple1)} Max:{max(tuple1)} Min:{min(tuple1)}")
    
    
if __name__ == "__main__":
    main()