AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def menu():
    print("*"*32)
    print("AutoCountry Vehicle Finder v0.1")
    print("*"*32)
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. Exit")

menu()
choice = int(input())
while choice !=3:
    
    if choice ==1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicle:")
        for car in AllowedVehiclesList:
            print(car)
    elif choice ==2:
        car = input('\033[1m'+"Please Enter the full Vehicle name: "+'\033[0m')
        if car in AllowedVehiclesList:
            print(car,"is an authorized vehicle")
        else: 
            print(car,"is not an authorized vehicle, if you received this in error please check the spelling and try again")
    menu()
    choice = int(input())
print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")