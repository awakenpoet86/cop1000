# Print menu 
def menu():
    print("*"*32)
    print("AutoCountry Vehicle Finder v0.6")
    print("*"*32)
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("*"*32)

# Print vehicles
def printVehicles(filename):
    with open(filename, 'r') as file:
        vehicles = file.read().splitlines()
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(vehicle)
    print()

# Search vehicle
def searchVehicle(filename,search_term):
    with open(filename, 'r') as file:
        vehicles = file.read().splitlines()
    if search_term in vehicles:
        print(f"\n{search_term} is an authorized vehicle.")
    else:
        print(f"\n{search_term} is not an authorized vehicle, please check the spelling and try again.")
    print()
#Add a vehicle
def addVehicle(filename,new_vehicle):
    with open(filename, 'a') as file:
        file.write(f"\n{new_vehicle}")
    print(f"\nYou have added '{new_vehicle}' as an authorized vehicle.")
    print()
# Remove a vehicle
def removeCar(filename, car):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Find and remove the line 
    for i, line in enumerate(lines):
        if line.strip() == car.strip():
            del lines[i]
            with open(filename, 'w') as file:
                file.writelines(lines)
            print(f"\nVehicle '{car.strip()}' removed successfully.")
            return
    print(f"\nVehicle '{car.strip()}' not found in the list.")


def main():
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 
                         'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
    filename = "vehicle.txt"
    
    
    while True:
        menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:  # PRINT all vehicles
                printVehicles(filename)
                
            elif choice == 2:  # SEARCH for vehicle
                search_term = input("\nEnter the full vehicle name to search: ").strip()
                searchVehicle(filename,search_term)
                
            elif choice == 3:  # ADD vehicle
                new_vehicle = input("\nEnter the full vehicle name you would like to add: ").strip()
                addVehicle(filename,new_vehicle)
                
            elif choice == 4:  # DELETE vehicle
                with open(filename, 'r') as file:
                    vehicles = file.read().splitlines()
               
                car = input("\nEnter the full vehicle name you would like to remove: ").strip()
                response = input('\033[1m'+"Are you sure you want to remove \""+ car +"\" from the Authorized Vehicles List? " +'\033[0m')
              
                if response == "yes":
                    removeCar(filename,car)
                
            elif choice == 5:  # EXIT
                print("\nThank you for using the AutoCountry Vehicle Finder. Goodbye!")
                break
                
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.\n")
                
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()