def operation(item,shopping_list,operation):
    if operation=='1':
        shopping_list.append(item)
        return "Item added"
    if operation=='2:
        if item in shopping_list:
            shopping_list.remove(item)
            return "Item deleted"
        else :return "Item does not exist in your list"
    if operation=='3':
        return shopping_list
      
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
            # Prompt for and add an item
            item=input("Enter your item to add : ").lower()
            print(operation(item,shopping_list,choice))
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item=input("Enter your item ").lower()
            print(operation(item,shopping_list,choice))
            pass
        elif choice == '3':
            # Display the shopping list
            print(operation(item,shopping_list,choice))
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
