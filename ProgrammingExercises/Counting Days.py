"""
Write a function called convert to days() that takes no parameters. Have your function prompt the user 
to input numbers of hours, minutes, and seconds. Write a helper function called get days() that uses these 
values and converts them to days in float form (fractions of a day are allowed). get days() should return the 
number of days. Use this helper function within the convert to days() function to display the numbers of 
days to the user. The built-in function round() takes two arguments: a number and an integer indicating 
the desired precision (i.e., the desired number of digits beyond the decimal point). Use this function to 
round the number of days four digits after the decimal point.
The following demonstrates the proper behavior of convert to days():
convert_to_days()
Enter number of hours: 97
Enter number of minutes: 54
Enter number of seconds: 45
The number of days is: 4.0797
"""
def convert_to_days():
    hour = int(input("Enter number of hours: "))
    min = int(input("Enter number of minutes: "))
    sec = int(input("Enter number of seconds: "))

    days = get_days(hour,min,sec)
    print(f"The number of days is: {days}")

def get_days(hour,min,sec):
    day = (hour + min/60 + sec/3600)/24
    return round(day,4)

convert_to_days()

