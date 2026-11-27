def calculate_parking():
    rates = {
        "two-wheeler": 20,
        "four-wheeler": 50,
        "heavy vehicle": 100
    }

    vehicle_number = input("Enter vehicle number: ").strip().upper()
    vehicle_type = input("Enter vehicle type (Two-wheeler / Four-wheeler / Heavy vehicle): ").strip().lower()
    
    if vehicle_type not in rates:
        print("Invalid vehicle type entered.")
        return

    try:
        duration = float(input("Enter parking duration in hours: "))
        if duration < 0:
            print("Duration cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for hours.")
        return

    total_fee = rates[vehicle_type] * duration

    print("\n--- Parking Receipt ---")
    print(f"Vehicle Number   : {vehicle_number}")
    print(f"Vehicle Type     : {vehicle_type.capitalize()}")
    print(f"Parking Duration : {duration} hours")
    print(f"Total Parking Fee: Rs. {total_fee:.2f}")

if __name__ == "__main__":
    calculate_parking()