def get_positive_number(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        text = input(prompt)
        try:
            value = float(text)
        except ValueError:
            print("Please enter numbers only, for example 70 or 1.75.")
            continue
        if value <= 0:
            print("The value must be greater than zero.")
            continue
        return value


def get_height():
    """Ask for height in metres, centimetres or feet, and return metres."""
    while True:
        unit = input("Height unit - m (metres), cm, or ft (feet): ").strip().lower()
        if unit in ("m", "cm", "ft"):
            break
        print("Please type m, cm or ft.")

    while True:
        height = get_positive_number(f"Enter your height in {unit}: ")
        if unit == "cm":
            height_m = height / 100
        elif unit == "ft":
            height_m = height * 0.3048
        else:
            height_m = height

        if 0.5 <= height_m <= 2.5:
            return height_m
        print("That height looks wrong for the unit you chose. Try again.")


def calculate_bmi(weight_kg, height_m):
    """BMI = weight / (height * height)."""
    return weight_kg / (height_m * height_m)


def get_category(bmi):
    """Return the health category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def ask_again():
    """Return True if the user wants to calculate again."""
    while True:
        answer = input("\nCalculate again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please type y or n.")


def main():
    print("=== BMI Calculator ===")
    while True:
        weight = get_positive_number("Enter your weight in kg: ")
        height = get_height()

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print(f"\nYour BMI is {bmi:.2f}")
        print(f"Category: {category}")

        if not ask_again():
            print("Goodbye! Stay healthy.")
            break


main()