def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            addition = input("Enter the name of the item you want to add: ")
            shopping_list.append(addition)
            pass
        elif choice == '2':
            removal = input("Enter the name of the item you want to remove: ")
            shopping_list.remove(removal)
            pass
        elif choice == '3':
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
