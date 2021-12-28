class ShoppingJW:

    #Initialiaze
    def __init__(self, foodname, foodamount):
        self.__foodname = foodname
        self.__foodamount = foodamount
        self.__standardprice = self.getPriceJW()
        self.__cost = self.getFoodCostJW()

    #The price list of the food
    def __PriceListJW(self):
        if self.__foodname == "Dry Cured Iberian Ham":
            self.__standardprice = 177.80
        elif self.__foodname == "Wagyu Steaks":
            self.__standardprice = 450.00
        elif self.__foodname == "Matsutake Mushrooms":
            self.__standardprice = 272.00
        elif self.__foodname == "Kopi Luwak Coffee":
            self.__standardprice = 306.50
        elif self.__foodname == "Moose Cheese":
            self.__standardprice = 487.20
        elif self.__foodname == "White Truffles":
            self.__standardprice = 3600.00
        elif self.__foodname == "Blue Fin Tuna":
            self.__standardprice = 3603.00
        elif self.__foodname == "Le Bonnotte Potatoes":
            self.__standardprice = 270.81
        else:
            self.__standardprice = 0

    #Get food name
    def getFoodNameJW(self): 
        return self.__foodname
    
    #Get food amount
    def getFoodAmountJW(self):
        return self.__foodamount
    
    #Get food price
    def getPriceJW(self):
        self.__PriceListJW()
        return self.__standardprice

    #Calculate the cost of the food together with the amount of that specific food  
    def getFoodCostJW(self):
        self.__cost = self.__standardprice * self.__foodamount
        return self.__cost