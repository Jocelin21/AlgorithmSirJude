"""
Enter a numerator: Value must be greater than 0: -3
Please re-enter the numerator. Value must be greater than 0: 3
Enter a denominator. Value must be greater than 0: -7
Please re-enter the denominator. Value must be greater than 0: 7
3 / 7 is a proper fraction.
This proper fraction cannot be reduced any further.

10 / 15 is a proper fraction.
This proper fraction can be reduced to: 2 / 3

78 / 11 is an improper fraction.
This improper fraction cannot be reduced any further.
The mixed number is 7 and 1 / 11
 
6 / 4 is an improper fraction.
This improper fraction can be reduced to: 3 / 2
The mixed number is 1 and 1 / 2
 
8 / 2 is an improper fraction.
This improper fraction can be reduced to: 4 / 1
The whole number is 4
 
11 / 1 is an improper fraction.
This improper fraction cannot be reduced any further.
The whole number is 11
"""
import math
num = int(input("Enter a numerator: Value must be greater than 0: "))
while num < 0:
    num = int(input("Please re-enter the numerator. Value must be greater than 0: "))
    
dem = int(input("Enter a denominator. Value must be greater than 0: "))
while dem < 0:
        dem = int(input("Please re-enter the denominator. Value must be greater than 0: "))

gcd = math.gcd(num,dem) 

if num < dem:
    print(f"{num} / {dem} is a proper fraction.")
    if gcd < 2:
        print("This proper fraction cannot be reduced any further.")
    else:
        num = int(num / gcd)
        dem = int(dem / gcd)
        print(f"This proper fraction can be reduced to: {num} / {dem}")
elif  num > dem:
    print(f"{num} / {dem} is an improper fraction.")
    mix = num // dem
    nums = num - mix*dem
    if gcd < 2:
        print("This improper fraction cannot be reduced any further.")
        if gcd != dem:
            print(f"The mixed number is {mix} and {nums} / {dem} ")
        else:
            print(f"The whole number is {mix}")
    else:
        num = int(num / gcd)
        nums = int(nums / gcd)
        dems = int(dem / gcd)
        print(f"This improper fraction can be reduced to: {num} / {dems}")
        if gcd != dem:
            print(f"The mixed number is {mix} and {nums} / {dems}")
        else:
            print(f"The whole number is {mix}")


 
    