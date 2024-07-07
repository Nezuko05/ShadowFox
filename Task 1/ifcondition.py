# 1. Write a program to determine the BMI Category based on user input. Ask the user to:
# Enter height in meters
# Enter weight in kilograms
# Calculate BMI using the formula: BMI = weight / (height)2
# Use the following categories:
# If BMI is 30 or greater, print "Obesity"
# If BMI is between 25 and 29, print "Overweight"
# If BMI is between 18.5 and 25, print "Normal"
# If BMI is less than 18.5, print "Underweight"
# Example:
# Enter height in meters: 1.75
# Enter weight in kilograms: 70
# Output: "Normal"

height=float(input("Enter height in metres"))
weight=float(input("Enter weight in kilogram"))
BMI= weight/height*height
if(BMI>=30):
    print("Obesity")
elif(BMI>25 and BMI<=29):
    print("Overweight")
elif(BMI>18.5 and BMI<=25):
    print("Normal")
elif(BMI<18.5):
    print("Underweight")
else:
    print("Wrong Input")    

#----------------------------------------------------------------------------------------------------#

# 2. Write a program to determine which country a city belongs to. Given list of cities per country:
# Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
# UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# Ask the user to enter a city name and print the corresponding country.
# Example:
# Enter a city name: "Abu Dhabi" 
# Output: "Abu Dhabi is in UAE"

Australia = ["sydney", "melbourne", "brisbane", "perth"]    
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]            
India = ["mumbai", "bangalore", "chennai", "delhi"] 
city_name=input("enter a city name")
if city_name in Australia:
    print("f{city_name} is in Australia")
elif city_name in UAE:
    print("f{city_name} is in UAE")
else:
    print("f{city_name} is in India")        

#------------------------------------------------------------------------------------------------#
# 
# 3. Write a program to check if two cities belong to the same country. 
# Ask the user to enter two cities and print whether they belong to the same country or not.
# Example:
# Enter the first city: "Mumbai"
# Enter the second city: "Chennai"
# Output: "Both cities are in India"
# Example:
# Enter the first city: "Sydney"
# Enter the second city: "Dubai"
# Output: "They don't belong to the same country"

Australia = ["sydney", "melbourne", "brisbane", "perth"]    #       ---------------------
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]            #       |   Defining List   |
India = ["mumbai", "bangalore", "chennai", "delhi"] 


first_city=input("Enter first city")
second_city=input("Enter second city")
if first_city in Australia and second_city in Australia:
    print("Both cities are in Australia")
elif first_city in UAE and second_city in UAE:
    print("Both cities are in UAE")
elif first_city in India and second_city in India:
    print("Both cities are in India")
else:
    print("They do not belong to the same country")             

#----------------------------------------------------------------------------------------------------#

    
