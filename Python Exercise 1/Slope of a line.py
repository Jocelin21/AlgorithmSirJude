"""
Write a program that prompts the user to enter the coordinates of two points (x1, y1) and (x2, 
y2). The program should calculate and display the slope of the line that connects the two points.
The formula for the slope is (y2-y1)/(x2-x1)
Format your output to five decimal places.
Sample output:
Enter the x-coordinate for point1: 4.5
Enter the y-coordinate for point1: -5.5
Enter the x-coordinate for point2: 6.6
Enter the y-coordinate for point2: -6.5
The slope for the line that connects two points ( 4.5 , -5.5 ) and ( 6.6 , -6.5 ) is -0.47619
"""
x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))

slope = (y2 - y1) / (x2 - x1)
slope_decimal = "{:.5f}".format(slope)

print (f"The slope for the line that connects two points ( {x1} , {y1} ) and ( {x2} , {y2} ) is {slope_decimal}.")