# function for linear search
def Linear_S(number, target):
    found = False
    for i in range(len(number)):
        if target == number[i]:
            print("Element found at index:", i)
            found = True
            break
    if not found:
        print("Element not present")


# function for binary search (list must be sorted)
def binary_S(number, target):
    low = 0
    high = len(number) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == number[mid]:
            print("Element found at index:", mid)
            break
        elif target > number[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print("Element not present")


# given array/list
n = int(input("Enter number of elements you want in the array: "))
number = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    number.append(element)

# user input
choice = int(input("Enter 1 for linear search\nEnter 2 for binary search: "))
target = int(input("Enter the element to be searched: "))

# checking user input
if choice == 1:
    Linear_S(number, target)
elif choice == 2:
    number.sort()  # sorting for binary search
    binary_S(number, target)
else:
    print("Wrong input")
