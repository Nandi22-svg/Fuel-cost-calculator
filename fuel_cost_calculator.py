# Fuel Cost Calculator
# Developed by Nandipha Mkhwanazi

def calculate_fuel_cost():
    print("=" * 40)
    print("       FUEL COST CALCULATOR")
    print("=" * 40)

    try:
        distance = float(input("Enter distance (km): "))
        consumption = float(input("Fuel consumption (L/100km): "))
        fuel_price = float(input("Fuel price per litre (R): "))

        if distance <= 0 or consumption <= 0 or fuel_price <= 0:
            print("\nError: Please enter positive numbers.")
            return

        litres_needed = (distance * consumption) / 100
        total_cost = litres_needed * fuel_price

        print("\n------ TRIP SUMMARY ------")
        print(f"Distance: {distance:.2f} km")
        print(f"Fuel needed: {litres_needed:.2f} litres")
        print(f"Fuel price: R{fuel_price:.2f}/L")
        print(f"Estimated trip cost: R{total_cost:.2f}")
        print("--------------------------")

    except ValueError:
        print("\nError: Please enter valid numbers.")

if __name__ == "__main__":
    calculate_fuel_cost()