
vehicle_type = input("Enter vehicle type: ")
hours = int(input("Enter parking hours: "))

if vehicle_type.lower() == "two-wheeler":
    rate = 20
elif vehicle_type.lower() == "four-wheeler":
    rate = 50
elif vehicle_type.lower() == "heavy vehicle":
    rate = 100
else:
    rate = 0

if rate == 0 or hours <= 0:
    print("Invalid input")
else:
    fee = rate * hours
    print("Vehicle Type:", vehicle_type)
    print("Parking Duration:", hours, "hours")
    print("Total Parking Fee: Rs.", fee)
