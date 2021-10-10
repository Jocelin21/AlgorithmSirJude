"""
Write a program that reads the subtotal and gratuity rate. The program then calculates and 
gratuity as a dollar amount, followed by the total amount, and displays all information in
dollars. 
Your code should include currency formatting (i.e., use the $ in your output, include comma 
separation and format the result to 2 decimal places.)
Sample output:
Enter the subtotal: $1250
Enter tip amount (as a %): 25
Subtotal: $ 1,250.00
Tip: $ 312.50
Total: $ 1,562.5
"""
subtotal_original = float(input("Enter the subtotal: $ "))
tip_original = float(input("Enter tip amount (as a %): ")) 

tip = subtotal_original*(tip_original/100)

total = "{:,.1f}".format(subtotal_original + tip)
subtotal = "{:,.2f}".format(subtotal_original)
tips = "{:,.2f}".format(tip)

print("Subtotal: $ ", subtotal)
print("Tip: $ ", tips)
print("Total: $ ", total)
