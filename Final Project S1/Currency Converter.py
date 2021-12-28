from tkinter import * #import everything from tkinter

#List of the available currencies: Australia, Canada, China, Europe, Indonesia, India, America
currency_list = ["AUD", "CAD", "CNH", "EUR", "IDR", "INR", "USD"]
 
def convert():
    #Getting the variable
    currency1 = variable1.get()
    currency2 = variable2.get()
    money_original = float(moneyOri.get())
    
    #Converting the currency
    if (currency1 == "AUD" and currency2 == "CAD"):
        result = money_original * 0.93
    elif (currency1 == "AUD" and currency2 == "CNH"):
        result = money_original * 4.60
    elif (currency1 == "AUD" and currency2 == "EUR"):
        result = money_original * 0.64
    elif (currency1 == "AUD" and currency2 == "IDR"):
        result = money_original * 10290.06
    elif (currency1 == "AUD" and currency2 == "INR"):
        result = money_original * 54.23
    elif (currency1 == "AUD" and currency2 == "USD"):
        result = money_original * 0.72
    elif (currency1 == "CAD" and currency2 == "AUD"):
        result = money_original * 1.08
    elif (currency1 == "CAD" and currency2 == "CNH"):
        result = money_original * 4.98
    elif (currency1 == "CAD" and currency2 == "EUR"):
        result = money_original * 0.69
    elif (currency1 == "CAD" and currency2 == "IDR"):
        result = money_original * 11108.11
    elif (currency1 == "CAD" and currency2 == "INR"):
        result = money_original * 58.54
    elif (currency1 == "CAD" and currency2 == "USD"):
        result = money_original * 0.78
    elif (currency1 == "CNH" and currency2 == "AUD"):
        result = money_original * 0.22
    elif (currency1 == "CNH" and currency2 == "CAD"):
        result = money_original * 0.20
    elif (currency1 == "CNH" and currency2 == "EUR"):
        result = money_original * 0.14
    elif (currency1 == "CNH" and currency2 == "IDR"):
        result = money_original * 2231.32
    elif (currency1 == "CNH" and currency2 == "INR"):
        result = money_original * 11.76
    elif (currency1 == "CNH" and currency2 == "USD"):
        result = money_original * 0.16
    elif (currency1 == "EUR" and currency2 == "AUD"):
        result = money_original * 1.57
    elif (currency1 == "EUR" and currency2 == "CAD"):
        result = money_original * 1.45
    elif (currency1 == "EUR" and currency2 == "CNH"):
        result = money_original * 7.22
    elif (currency1 == "EUR" and currency2 == "IDR"):
        result = money_original * 16105.12
    elif (currency1 == "EUR" and currency2 == "INR"):
        result = money_original * 84.87
    elif (currency1 == "EUR" and currency2 == "USD"):
        result = money_original * 1.13
    elif (currency1 == "IDR" and currency2 == "AUD"):
        result = money_original * 0.000097
    elif (currency1 == "IDR" and currency2 == "CAD"):
        result = money_original * 0.000090
    elif (currency1 == "IDR" and currency2 == "CNH"):
        result = money_original * 0.00045
    elif (currency1 == "IDR" and currency2 == "EUR"):
        result = money_original * 0.000062
    elif (currency1 == "IDR" and currency2 == "INR"):
        result = money_original * 0.0053
    elif (currency1 == "IDR" and currency2 == "USD"):
        result = money_original * 0.000070
    elif (currency1 == "INR" and currency2 == "AUD"):
        result = money_original * 0.018
    elif (currency1 == "INR" and currency2 == "CAD"):
        result = money_original * 0.017
    elif (currency1 == "INR" and currency2 == "CNH"):
        result = money_original * 0.085
    elif (currency1 == "INR" and currency2 == "EUR"):
        result = money_original * 0.012
    elif (currency1 == "INR" and currency2 == "IDR"):
        result = money_original * 189.76
    elif (currency1 == "INR" and currency2 == "USD"):
        result = money_original * 0.013
    elif (currency1 == "USD" and currency2 == "AUD"):
        result = money_original * 1.38
    elif (currency1 == "USD" and currency2 == "CAD"):
        result = money_original * 1.28
    elif (currency1 == "USD" and currency2 == "CNH"):
        result = money_original * 6.37
    elif (currency1 == "USD" and currency2 == "EUR"):
        result = money_original * 0.88
    elif (currency1 == "USD" and currency2 == "IDR"):
        result = money_original * 14216.70
    elif (currency1 == "USD" and currency2 == "INR"):
        result = money_original * 74.92
    else:
        result = money_original
    
    #Set the total
    total.set(result)

#Make window
tk = Tk()
tk.title("Currency Converter")
tk.geometry("400x250")
 
#Setting the currency 
variable1 = StringVar(tk)
variable1.set(currency_list[0])
variable2 = StringVar(tk)
variable2.set(currency_list[1])

#First dropdown menu button
currencyOpt1 = OptionMenu(tk, variable1, *currency_list)
currencyOpt1.config(width=10, fg = '#282828', font=('Helvetica', 12))
currencyOpt1.place(x = 40, y = 10)
currencyOpt1.pack(pady = 5)

#Input the amount of money
moneyOri = Entry(tk)
moneyOri.pack(side="top", pady = 4)

#Second dropdown menu button
currencyOpt2 = OptionMenu(tk, variable2, *currency_list)
currencyOpt2.config(width=10, fg = '#282828', font = ('Helvetica', 12))
currencyOpt2.place(x = 40, y = 80)
currencyOpt2.pack()

#From-To labels
from_label = Label(tk, text = "From", fg = '#282828', font = ('Helvetica', 12)).place(x=40, y=10)
to_label = Label(tk, text = "To", fg = '#282828', font = ('Helvetica', 12)).place(x=40, y=80)
total_label = Label(tk, text="Total:", fg = '#282828', font = ('Helvetica', 12)).place(x=40, y=155)

#Convert Button
convertButton = Button(tk, text = "Calulate", command = convert)
convertButton.config(height = 1, width = 10, fg = '#282828', font = ('Helvetica', 12))
convertButton.pack(pady = 8)

#The result of the converted money
total = StringVar()
money_converted = Label(tk, text = "", textvariable = total)
money_converted.config(fg = '#282828', font = ('Helvetica', 12))
money_converted.pack(pady = 2)

#To start the window
tk.mainloop()