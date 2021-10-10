"""
Write a program that prompts the user to enter the side of a hexagon and displays its area. The
area of a hexagon is (3v3)/2 x s^2

Assume that the side entered is positive.
Format the result to three decimal places. Use the functions pow and sqrt from the math 
module to express the formula accurately. (See section 2.9 in your zyBook to review the math 
module.)
Sample output:
Enter the side length of the hexagon: 5.5
The area of a hexagon with side length 5.5 is 78.592
"""
length = float(input("Enter the side length of the hexagon: "))
area = 3*3**(1/2)/2 * length ** 2
areas = ("{:.3f}".format(area))

print("The area of a hexagon with side length 5.5 is ", areas)