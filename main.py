
#algorithm menu program
choice = int(input("""
Choose which program you would like to use from the selected : 

=== ALGORITHM VISUALIZER ===

1. Linear Search
2. Binary Search
3. Bubble Sort
4. Exit 
"""))

if choice == 1:
    print("Linear Search selected! ")
elif choice == 2:
    print("Binary Search selected! ")
elif choice == 3:
    print("Bubble Sort selected! ")
elif choice == 4:
    print("Goodbye! ")
else:
    print("Your input is not one of the options...")
