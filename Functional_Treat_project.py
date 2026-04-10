datastore=[]

def input_data():
    global datastore
    datastore= list(map(int, input("\nEnter data for 1D array (separated by spaces): ").split()))
    print("Data has been stored successfully!")

def display_summary():
    print("\nDATA SUMMARY:")
    print("-Total elements:", len(datastore))
    print("-Minimum Value:", min(datastore))
    print("-Maximum Value:", max(datastore))
    print("-Sum of all values:", sum(datastore))
    print("-Average Value:", round(sum(datastore)/len(datastore), 2))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def filter_data():
    t=int(input("Enter a threshold value to filter out data above this value:\n"))
    result=list(filter(lambda x: x >= t, datastore))
    print(f"\nFiltered data (value >= {t})")
    print(", ".join(map(str, result)))

def sort_data():
    print("\nChoose Sorting option:")
    print("1. Ascending")
    print("2. Descending")
    ch=int(input("\nEnter your choice:"))
    if ch==1:
        s=sorted(datastore)
        print("\nSorted Data in Ascending Order:")
    else:
        s=sorted(datastore, reverse=True)
        print("\nSorted Data in Descending Order:")
    print(", ".join(map(str, s)))

def dataset_stats():
    l= min(datastore)
    h= max(datastore)
    s= sum(datastore)
    avg= round(sum(datastore)/len(datastore), 2)
    return l, h, s, avg

print("WELCOME to the DATA ANALYZER and TRANSFORMER:)")

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice=int(input("Enter your choice here:"))

    if choice==1:
        input_data()

    elif choice==2:
        display_summary()

    elif choice==3:
        n=int(input("\nEnter a number to calculate its factorial:"))
        print(f"Factorial of {n} is:", factorial(n))

    elif choice==4:
        filter_data()

    elif choice==5:
        sort_data()

    elif choice==6:
        l, h, s, avg= dataset_stats()
        print("\nDataset Statistics:")
        print("-Minimum Value:", l)
        print("-Maximum Value:", h)
        print("-Sum of all values:", s)
        print("-Average Value:", avg)

    elif choice==7:
        print("Exiting The program. Thank you for using this program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please choose again")