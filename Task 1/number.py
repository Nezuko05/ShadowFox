# 1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string.
#    Print the result. Try to identify the representation used.
def formatfunc(num,letter):
    return format(num,letter)
print(formatfunc(145,"o"))
# It is returning 221 as the formatted result
#------------------------------------------------------------------------------------------------#

# 2.  In a village, there is a circular pond with a radius of 84 meters. 
# Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
# Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? 
# Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

pi=3.14
radius=84
Area=int(pi*radius*radius)
total_amount_of_water=int(Area*1.4)
print(f"total area of pond is {Area}and total amount of water is {total_amount_of_water}")
# The Output is "The total pond area is 22155 and the total water in the pond is 31016"

#----------------------------------------------------------------------------------------------#

# 3. If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second. 
#    Print the answer without any decimal point in it. Hint: Speed = Distance / Time
distance=490
time=7
speed=int(distance/time)
print(f"the speed is {speed}")
# The calculated speed is 70

#----------------------------------------------------------------------------------------------------#



