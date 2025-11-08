empID = list(map(int,input("Enter Employees IDs seprated by space:").split()))
def linear_search(empID,target):
    for i in range(len(empID)):
        if empID[i]==target:
            return i
    return -1
    
def binary_search(empID,target):
    sorted_empID = sorted (empID)
    low = 0
    high = len(sorted_empID) - 1
    
    while low <= high:
        mid = (low + high)//2
        if sorted_empID[mid] == target:
                    return mid , sorted_empID
        elif sorted_empID[mid] < target:
                    low = mid + 1
        else:
                high = mid - 1
        return -1 , sorted_empID

def menu():
    print ("/n===MENU===")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")
    
    
while True:
        menu()  #display menu
        choice = input("enter choice:")
        #if user select linear search
        if choice == '1':
            key = int(input("Enter ID to be searched(Linear Search):"))
            res = linear_search(empID , key)
            if res != -1:
                 print(f"element found at index {res}")
            else:
                 print("not found")
                 
     #if user select binary search
        if choice == '2':        
            key = int(input("enter ID to be searched(Binary Search):"))
            res, sorted_list = binary_search(empID , key)
            print("sorted list used for binary search:" , sorted_list)
            if res != -1:
                print(f"element found at index {res} (sorted_list)")
            else:
                    print("not found")
                    
     #if user choose to exit
        elif choice == '3':                    
            print("exiting program")
            break
    #if user enters invalid option
        else:
            print("invalid choice. please try again.")
                    
                    
                    
                    
                    
                    
                    
                    
    
    
    
    
    