
def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def feet_to_inches(feet):
    return feet * 12

def inches_to_feet(inches):
    return inches / 12

def main():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Feet to Inches")
    print("4. Inches to Feet")

    choice = input("Please select the type of conversion (1/2/3/4): ")

    try:
        if choice == "1":
            value = float(input("Enter the length in meters: "))
            result = meters_to_feet(value)
            print(f"{value} meters is equal to {result} feet")

        elif choice == "2":
            value = float(input("Enter the length in feet: "))
            result = feet_to_meters(value)
            print(f"{value} feet is equal to {result} meters")

        elif choice == "3":
            value = float(input("Enter the length in feet: "))
            result = feet_to_inches(value)
            print(f"{value} feet is equal to {result} inches")

        elif choice == "4":
            value = float(input("Enter the length in inches: "))
            result = inches_to_feet(value)
            print(f"{value} inches is equal to {result} feet")

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4 for the conversion type.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for length.")

if __name__ == "__main__":
    main()
