from admin import AdminActions
from customer import CustomerActions

def main():
    while True:
        print("User Type Selection:")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")
        
        user_option = input("Enter your choice (1=Admin, 2=Customer, 3=Exit): ")
        if user_option == "1":
            admin_actions = AdminActions()
            while True:
                print("Admin Actions:")
                print("1. Display Menu")
                print("2. Add product")
                print("3. Update Product")
                print("4. Delete Product")
                print("5. Search Product")
                print("6. Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    admin_actions.display_menu()
                elif choice == 2:
                    admin_actions.add_product()
                elif choice == 3:
                    admin_actions.update_product()
                elif choice == 4:
                    admin_actions.delete_product()
                elif choice == 5:
                    admin_actions.search_product()
                elif choice == 6:
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif user_option == "2":
            customer_actions = CustomerActions()
            while True:
                print("Customer Actions:")
                print("1. Display Menu")
                print("2. Place Order")
                print("3. View Total Bill")
                print("4. Exit")
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    customer_actions.display_menu()
                elif choice == 2:
                    customer_actions.place_order()
                elif choice == 3:
                    customer_actions.pay_bill()
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif user_option == "3":
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3")
            
main()
