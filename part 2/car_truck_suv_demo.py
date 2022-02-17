# This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6


def main():
    vehicles_list = []

    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input("Enter your choice: "))

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            car_brand = input("Enter car Brand: ")
            car_year = input("Enter car year: ")
            car_milage = input("enter car milage: ")
            car_price = input("Enter car price: ")
            car_doors = input("Enter amount of doors on car: ")
            vehicles_list.append(
                vehicles.Car(car_brand, car_year, car_milage, car_price, car_doors)
            )

        elif choice == NEW_TRUCK_CHOICE:
            truck_brand = input("Enter truck Brand: ")
            truck_year = input("Enter truck year: ")
            truck_milage = input("enter truck milage: ")
            truck_price = input("Enter truck price: ")
            truck_drive = input("Enter truck drive: ")
            vehicles_list.append(
                vehicles.Truck(
                    truck_brand, truck_year, truck_milage, truck_price, truck_drive
                )
            )

        elif choice == NEW_SUV_CHOICE:
            SUV_brand = input("Enter SUV Brand: ")
            SUV_year = input("Enter SUV year: ")
            SUV_milage = input("enter SUV milage: ")
            SUV_price = input("Enter SUV price: ")
            SUV_capacity = input("Enter SUV capacity: ")
            vehicles_list.append(
                vehicles.SUV(SUV_brand, SUV_year, SUV_milage, SUV_price, SUV_capacity)
            )

        elif choice == FIND_VEHICLE_CHOICE:
            check = str(input("Find vehicle by name: "))
            for elem in vehicles_list:
                if check in elem.brand:
                    print(elem)

        elif choice == SHOW_VEHICLES_CHOICE:
            # show all vehicles
            print("The following cars are in inventory:")
            for item in vehicles_list:
                print(item)

        elif choice == QUIT_CHOICE:
            print("Exiting the program...")

        else:
            print("Error: invalid selection.")


# The display_menu function displays a menu.
def display_menu():
    print("        MENU")
    print("1) New car")
    print("2) New truck")
    print("3) New SUV")
    print("4) Find vehicles by make")
    print("5) Show all vehicles")
    print("6) Quit")


# Call the main function.
if __name__ == "__main__":
    main()
