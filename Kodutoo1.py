# Function to calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


# Function to assess BMI result
def assess_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Simple loop to continue as long as the user wants
continue_calculation = "yes"
while continue_calculation == "yes":
    # Asking for user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculating BMI and assessing the result
    bmi = calculate_bmi(weight, height)
    result = assess_bmi(bmi)

    # Displaying the result
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
    print(f"This means: {result}")

    # Asking the user if they want to perform another calculation
    continue_calculation = input("Do you want to calculate again? (yes/no): ").lower()

print("Exiting the program.")
