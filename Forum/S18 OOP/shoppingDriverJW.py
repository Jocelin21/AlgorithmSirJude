from shoppingClassJW import ShoppingJW

#Getting user's input and making the list
def userlistJW():
    foodlist = ["Dry Cured Iberian Ham", "Wagyu Steaks", "Matsutake Mushrooms", "Kopi Luwak Coffee",
                "Moose Cheese", "White Truffles", "Blue Fin Tuna", "Le Bonnotte Potatoes"]
    shoppinglist = [] 
    itemNum = int(input("How many items will you order today? "))
    #Ask again if they answer below 1
    while itemNum < 1: 
        print("Number of items must be at least 1.")
        itemNum = int(input("How many items will you order today? "))

    i = 1
    while i < itemNum+1:
        print(f"Item #{i}-")
        food = str(input("Enter food: "))

        #Ask again if they insert a food that is not on the menu
        while food not in foodlist:
            print("The food is not in the list.")
            food = str(input("Enter food: "))

        amount = float(input("Enter amount of pounds: "))

        #Ask again if they answer less or equal to 0
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))
        print()
        i += 1
        
        data = ShoppingJW(food, amount)
        shoppinglist.append(data) 
    #Return the list with the food names and amount
    return shoppinglist 

#The summary list
def summaryJW(list):
    print("Here's a summary of the items purchased:")
    print("----------------------------------------")
    for food in range(len(list)): 
        print(f"Item: {list[food].getFoodNameJW()}") 
        print(f"Amount ordered: {list[food].getFoodAmountJW()} pounds")
        print(f"Price per pound: {'{:.2f}'.format(list[food].getPriceJW())}")
        print(f"Price of order: {'{:.2f}'.format(list[food].getFoodCostJW())}")
        print()

#The total of everything
def totalJW(list): 
    total = 0.00
    for food in range(len(list)): 
        total += list[food].getFoodCostJW()
    return total

#The function that runs everything
def main():
    result = userlistJW()
    summaryJW(result)
    print(f"Total cost: {'{:.2f}'.format(totalJW(result))}")

#To run it 
main()
