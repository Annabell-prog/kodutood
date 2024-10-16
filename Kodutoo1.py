# Function to calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    # Calculating BMI by dividing weight (kg) by height squared (m^2)
    bmi = weight / (height ** 2)
    return bmi


# Function to assess BMI result
def assess_bmi(bmi):
    # If BMI is less than 18.5, the person is considered underweight
    if bmi < 18.5:
        return "Underweight"
    # If BMI is between 18.5 and 24.9, the person has a normal weight
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    # If BMI is between 25 and 29.9, the person is considered overweight
    elif 25 <= bmi < 29.9:
        return "Overweight"
    # If BMI is 30 or above, the person is considered obese
    else:
        return "Obesity"


# Simple loop to continue as long as the user wants
continue_calculation = "yes"
while continue_calculation == "yes":
    # Asking for user input - weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))
    # Asking for user input - height in meters
    height = float(input("Enter your height in meters: "))

    # Calculating BMI and assessing the result
    bmi = calculate_bmi(weight, height)  # Calling function to calculate BMI
    result = assess_bmi(bmi)  # Calling function to assess BMI category

    # Displaying the result
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")  # Displaying BMI value to 2 decimal places
    print(f"This means: {result}")  # Displaying the BMI assessment result

    # Asking the user if they want to perform another calculation
    continue_calculation = input("Do you want to calculate again? (yes/no): ").lower()  # Getting user input for another calculation

# Printing a message when exiting the program
print("Exiting the program.")
