"""
 software company sells a package that retails for $99. Discounts for quantities are given 
according to the following table:
Quantity Discount
 10 -19    10%
 20 - 49   20%
 50 - 99   30%
 100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program 
should then display the amount of the discount (if any) and the total of the purchase after the 
discount. (Use appropriate formatting to display currency and percentages in your output.)
Sample output (no discount):
Enter the number of packages purchased: 5
Discount Amount @ 0% : $ 0.00
Total Amount: $ 495.00
Sample output (with a discount):
Enter the number of packages purchased: 45
Discount Amount @ 20% : $ 891.00
Total Amount: $ 3564.00
"""
quantity = int(input("Enter the number of packages purchased:  "))

if quantity < 0:
    print("Quantity is out of range.")
elif quantity >= 0 and quantity <= 10:
    discount = 0
elif quantity >= 10 and quantity <= 19:
    discount = 10
elif quantity >= 20 and quantity <= 49:
    discount = 20
elif quantity >= 50 and quantity <= 99:
    discount = 30
else:
    discount = 40

discounted = "{:.2f}".format(99 * quantity * (discount/100))
total = "{:.2f}".format(99 * quantity - float(discounted))

print(f"Discount amount @ {discount}% : $ ", discounted)
print("Total amount: $ ", total)