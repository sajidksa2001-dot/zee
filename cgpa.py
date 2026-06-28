def sort_numbers():
    # You can change these numbers to whatever you like!
    numbers = [42, 7, 19, 95, 3, 28, 14, 88, 5]
    
    print("\n" + "="*40)
    print(f"Original List:  {numbers}")
    
    # Sorting the list in ascending order
    numbers.sort()
    
    print(f"Sorted List:    {numbers}")
    print("="*40 + "\n")

if __name__ == "__main__":
    sort_numbers()