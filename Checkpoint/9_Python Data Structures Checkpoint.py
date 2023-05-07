shopping_list = []

while True:
    print("Please select the desired option from below:\n\
          1. Add items\n\
          2. Remove items\n\
          3. View items\n\
          4. Quit program")
    option = input("Your desired option: ")

    # adding items
    if option == '1':
        item = input("Please enter the item you want to add: ")
        if len(shopping_list) in range(10):
            if item in shopping_list:
                print(f"{item} is already in the list.")
            else:
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
        else:
            print("Sorry, list is full.")

    # removing items
    elif option == '2':
        item = input("Please enter the item you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed froom the list.")
        else:
            print(f"Sorry, but {item} is not in the list.")

    # listing items
    elif option == '3':
        if not shopping_list:
            for item in shopping_list:
                print(f"* {item}")
        else:
            print("List is empty.")

    # quiting app
    elif option == '4':
        print("Application Closing...")
        break
    
    #wrong input
    else:
        print("Invalid option, please try again.")