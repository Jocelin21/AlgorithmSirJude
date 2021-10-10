"""
Given an airplane’s acceleration, a, and take-off speed, v, the minimum runway length needed 
for the airplane to take off is computed using the formula v^2/2a
Write a program that prompts the user to enter the speed in meters per second (m/s) and the 
acceleration in meters per second squared (m/s2
). The program should calculate and display the 
minimum runway length. Format the result to four decimal places. (For this question, assume
that all values entered are positive.)
Sample output:
Enter the plane's take off speed in m/s: 60
Enter the plane's acceleration in m/s**2: 3.5
The minimum runway length needed for this airplane is 514.2857 meters.
"""
speed = float(input("Enter the plane's take off speed in m/s: "))
acceleration = float(input("Enter the plane's acceleration in m/s**2: "))

distance = speed**2/(2*acceleration)
distance_decimal = "{:.4f}".format(distance)

print(f"The minimum runway length needed for this airplane is {distance_decimal} meters.")