
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

    length = int(input(" How many numbers are in your array? "))

    for x in range(length):
        binary_search = int(input(" Enter number " + str( x + 1 ) + " :"))
        list_numbers.append(binary_search)
    print(f"Your sequence is {list_numbers}.")

    start_index = 0
    end_index = int(len(list_numbers)-1)


    target_bin = int(input("What is your target value? "))



    #looking for if target is greater than middle index
    while start_index <= end_index:
        
        new_middle_index = int((start_index+end_index)//2)

            #looking for target value starting from middle
        if list_numbers[new_middle_index] == target_bin:
            print(f"The target was found at index {new_middle_index}!")
            found = True
            break

        #loops through
        elif target_bin > list_numbers[new_middle_index]:
            start_index = new_middle_index + 1

        else: 
            end_index = new_middle_index - 1
    
    if not found:
        print(f"Sorry your target: {target_bin} was not found.")



elif menu_choice == 3:
    print("Bubble Sort selected! ")


    length = int(input(" How many numbers are in your array? "))

    for x in range(length):
        bubble_sort = int(input(" Enter number " + str( x + 1 ) + " :"))
        list_numbers.append(bubble_sort)
    print(f"Your sequence is {list_numbers}.")

    #sorting the list
    def bubble_sort(numbers):
        n = len(numbers)
        comparisons = 0
        swaps = 0


        #multiple passes thru list
        for x in range(n):
                
             #is it sorted?
            is_sorted = True

            #swap
            for y in range(0, n - x - 1):

                #checks how many comparisons
                comparisons += 1

                if numbers[y] > numbers[y+1]:
                    numbers[y] , numbers[y+1] = numbers[y+1] , numbers[y]

                    #how many swaps
                    swaps += 1
                    is_sorted = False

            print(f"Pass {x + 1}: {numbers}")


            if is_sorted:
                print("List is sorted. No swaps are made.")
                break      
        print("\n===== Statistics =====")
        print(f"Comparisons: {comparisons}")
        print(f"Swaps: {swaps}")

        return numbers
    
    bubble_sort(list_numbers)
    print(f"\nSorted list: {list_numbers}")
            
elif menu_choice == 4:
    print("Selection Sort selected! ")

    length = int(input(" How many numbers are in your array? "))

    for x in range(length):
        select_sort = int(input(" Enter number " + str( x + 1 ) + " :"))
        list_numbers.append(select_sort)
    print(f"Your sequence is {list_numbers}.")


    def select_sort(numbers):
        n = len(numbers)

        #first loop assume x is min
        for x in range(n - 1):
            min_index = x

            #if later position is smaller swap
            for y in range(x + 1, n):
                if numbers[y] < numbers[min_index]:
                   min_index = y

            #make list sorted
            if min_index != x:
                temp = numbers[x]
                numbers[x] = numbers[min_index]
                numbers[min_index] = temp
    
        return numbers
    
    select_sort(list_numbers)
    print(f"\nSorted list: {list_numbers}")

elif menu_choice == 5:
    print("Insertion sort selected. ")

    length = int(input("How many numbers are in your array? "))

    for x in range(length):
        number = int(input("Enter number " + str(x + 1) + ": "))
        list_numbers.append(number)

    print(f"Original sequence: {list_numbers}")

    #insertion
    def insertion_sort(numbers):

        #how many comparisons how many shifts
        comparisons = 0
        shifts = 0

        for i in range(1, len(numbers)):

            key = numbers[i]
            j = i - 1

            #check if number is greater than
            while j >= 0 and numbers[j] > key:
                comparisons += 1
                numbers[j + 1] = numbers[j]
                shifts += 1
                j -= 1

            if j >= 0:
                comparisons += 1

            numbers[j + 1] = key

            print(f"Pass {i}: {numbers}")

        print("\n===== Statistics =====")
        print(f"Comparisons: {comparisons}")
        print(f"Shifts: {shifts}")

        return numbers

    insertion_sort(list_numbers)

    print(f"\nSorted list: {list_numbers}")

elif menu_choice == 6:
    print("Goodbye! ")
else:
    print("Your input is not one of the options...")
