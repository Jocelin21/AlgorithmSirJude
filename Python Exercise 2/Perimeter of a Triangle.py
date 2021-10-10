"""
Write a program that reads the three edges of a triangle and computes the perimeter if the 
input is valid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Otherwise (i.e. else) print a message stating that the input is invalid and the 
perimeter cannot be calculated. (Note: This question does NOT require further input 
validation.)

Sample output (Valid case):
Enter length of edge1: 6.7
Enter length of edge2: 9.2
Enter length of edge3: 11.6
The perimeter is 27.5
Sample output (Invalid case):
Enter length of edge1: 16
Enter length of edge2: 4.5
Enter length of edge3: 23.5
Perimeter cannot be calculated: the input is invalid.
"""
l1 = float(input("Enter the legth of edge1: "))
l2 = float(input("Enter the legth of edge2: "))
l3 = float(input("Enter the legth of edge3: "))

if l1 + l2 >= l3 and l2 + l3 >= l1 and l1 + l3 >= l2:
    print("The perimeter is ", l1 + l2 + l3)
else:
    print("Perimeter cannot be calculated: the input is invalid.")