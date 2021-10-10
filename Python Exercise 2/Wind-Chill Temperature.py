"""
In 2001, the National Weather Service implemented a new wind-chill temperature formula to 
measure the coldness using temperature and wind speed. The formula is:
twc = 35.74 + 0.621ta - 35.75v^0.16 + 0.4275tav^0.16
where:
twc is the wind chill temperature
ta is the outside temperature
v is the wind speed

The formula can only be used for temperatures between -58 degrees Fahrenheit and 41 
degrees Fahrenheit, as well as wind speeds greater than or equal to 2mph.

Write a program that:
• asks the user to enter a temperature between -58 degrees Fahrenheit and 41 degrees 
Fahrenheit.
    Input validation: If the user enters a temperature not in range, use an if 
statement or while loop to ask them to re-enter the value.
• asks the user to enter a windchill greater than 2mph.
    Input validation: If the user enters a wind speed not in range, use an if statement 
or while loop to ask them to re-enter the value. 
The program then calculates the wind-chill temperature using the formula above. Format the 
output to 3 decimal places.

Sample output (including input validation):
Enter the temperature in Fahrenheit: -60
Temperature must be between -58F and 41F
Please re-enter the temperature in Fahrenheit: 50
Temperature must be between -58F and 41F
Please re-enter the temperature in Fahrenheit: 35
Enter the wind speed miles per hour: -1
Speed must be greater than or equal to 2
Please re-enter the wind speed miles per hour: 5
The wind chill index is 30.600
"""
temp = float(input("Enter the temperature in Fahrenheit: "))
while temp < -58 or temp > 41:
    print ("Temperature must be between -58F and 41F")
    temp = float(input("Enter the temperature in Fahrenheit: "))

speed = float(input("Enter the wind speed miles per hour: "))
while speed < 2:
    print ("Speed must be greater than or equal to 2")
    speed = float(input("Please re-enter the wind speed miles per hour: "))

twc = "{:.3f}".format(35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16)

print("The wind chill index is ", twc)
