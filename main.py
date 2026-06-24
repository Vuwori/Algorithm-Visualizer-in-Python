
#algorithm menu program
menu_choice = int(input("""
Choose which program you would like to use from the selected : 

=== ALGORITHM VISUALIZER ===

1. Linear Search
2. Binary Search
3. Bubble Sort
4. Exit 
"""))

list_numbers = []

if menu_choice == 1:
    print("Linear Search selected! ")

    length = int(input(" How many numbers are in your array? "))
    for x in range(length):
        
        linear_search = int(input(" Enter number " + str( x + 1 ) + " :"))

        list_numbers.append(linear_search)

    print(f"Your sequence is {list_numbers}.")
        
    target_value = int(input("What is the target value? "))

    #looking for a specific value
    for x in range(len(list_numbers)):
        if list_numbers[x] == target_value:
            print(f"Your target number is at index {x}.")


elif menu_choice == 2:
    print("Binary Search selected! ")
elif menu_choice == 3:
    print("Bubble Sort selected! ")
elif menu_choice == 4:
    print("Goodbye! ")
else:
    print("Your input is not one of the options...")

#linear search
