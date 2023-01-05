from datetime import datetime
import random

now = datetime.now()
 

txt= "Vending Machine"
centre_txt= txt.center(63)

class Menu:
    
    def __init__(self, serialnumber, itemname, price):
        self.srno= serialnumber
        self.item= itemname
        self.price= price
        
    def DisplayMenu(self):
        print("  ", self.srno, "  ", self.item,   "         ", self.price)
    
            
    
    
    
menu0= Menu("0  ","Lays- Salt and Vinegar   ", "3.50 AED")
menu1= Menu("1  ","Doritos- Sweet and Chilli", "2 AED")
menu2= Menu("2  ","Pringles- BBQ Flavor     ", "5.50 AED")
menu3= Menu("3  ","Lays- Salt and Vinegar   ", "1.75 AED")

menu4= Menu("4  ","Snickers                 ", "3 AED")
menu5= Menu("5  ","Mars                     ", "2.50 AED")
menu6= Menu("6  ","Kitkat                   ", "2 AED")
menu7= Menu("7  ","Toblerone                ", "3.50 AED")

menu8= Menu("8  ","Melco(Mango)             ", "1.50 AED")
menu9= Menu("9  ","Avacado Mix              ", "7 AED")
menu10=Menu("10 ","Capri Sun(cocktail)      ", "2.50 AED")
menu11=Menu("11 ","Lacnor(Orange)           ", "2 AED")

menu12=Menu("12 ","Chocolate Milk           ", "2.50 AED")
menu13=Menu("13 ","Laban                    ", "1 AED")
menu14=Menu("14 ","Greek Yogurt             ", "5.50 AED")
menu15=Menu("15 ","Banana Milk              ", "2.50 AED")

menu16=Menu("16 ","Coca Cola                ", "3.50 AED")
menu17=Menu("17 ","Vimto                    ", "2.25 AED")
menu18=Menu("18 ","Mountain Dew             ", "3.50 AED")
menu19=Menu("19 ","7-Up                     ", "2 AED")

menu20=Menu("20 ","Espresso                 ", "4.50 AED")
menu21=Menu("21 ","Cappuccino               ", "4 AED")
menu22=Menu("22 ","Karak Tea                ", "1 AED")
menu23=Menu("23 ","Americano                ", "8 AED")


print(centre_txt)
print("\n\t\t\tChips")
menu0.DisplayMenu()
menu1.DisplayMenu()
menu2.DisplayMenu()
menu3.DisplayMenu()

print("\n\t\t\tChocolates")
menu4.DisplayMenu()
menu5.DisplayMenu()
menu6.DisplayMenu()
menu7.DisplayMenu()

print("\n\t\t\tJuices")
menu8.DisplayMenu()
menu9.DisplayMenu()
menu10.DisplayMenu()
menu11.DisplayMenu()

print("\n\t\t\tDairy Products")
menu12.DisplayMenu()
menu13.DisplayMenu()
menu14.DisplayMenu()
menu15.DisplayMenu()

print("\n\t\t\tCold Drinks")
menu16.DisplayMenu()
menu17.DisplayMenu()
menu18.DisplayMenu()
menu19.DisplayMenu()

print("\n\t\t\tHot Drinks")
menu20.DisplayMenu()
menu21.DisplayMenu()
menu22.DisplayMenu()
menu23.DisplayMenu()


item0= 3.5
item1= 2
item2= 5.5
item3= 1.75

item4= 3
item5=2.5
item6= 2
item7= 3.5

item8= 1.5
item9= 7 
item10= 2
item11= 2

item12= 2.5
item13= 1
item14= 5.5
item15=2.5

item16=3.5
item17=2.25
item18= 3.5
item19=2

item20=4.5
item21=4
item22=1
item23=8



menu={"0":"Lays- Salt and Vinegar",
      "1":"Doritos- Sweet Chilli)",
      "2": "Pringles- BBQ Flavor",
      "3": "Salad Chips",
      "4": "Snickers",
      "5": "Mars",
      "6": "KitKat",
      "7": "Toblerone",
      "8": "Melco(Mango)",
      "9": "Avacado Mix",
      "10": "Capri Sun(Cocktail)",
      "11": "Lacnor(Orange)",
      "12": "Chocolate Milk",
      "13": "Laban",
      "14": "Greek Yogurt",
      "15": "Banana Milk",
      "16": "Coca Cola",
      "17": "Vimto",
      "18": "Mountain Dew",
      "19": "7-Up",
      "20": "Espresso",
      "21": "Cappuccino",
      "22": "Karak Tea",
      "23": "Americano"}

#PriceofDrinks= item9+item10+item11+item12+item13+item14+item15+item16+item17+item18+item19+item20+item21+item22+item23

budget=int(input("\nEnter your budget: "))
option=input("Please select your desirable item according to the number: ")

amount=0
if option=='0' or option=="7" or option=="18":
    amount= budget - float(item0)
elif option=='1' or option=="6" or option=="11":
    amount= budget - float(item1)
elif option=="2" or option=="14":
    amount= budget - float(item2)
elif option=="3":
    amount= budget - float(item3)
elif option=='4':
    amount= budget - float(item2)
elif option=="5" or option=="10" or option=="12" or option =="15":
    amount= budget - float(item6)
elif option=="8":
    amount= budget - float(item8)
elif option=="9":
    amount= budget - float(item4)
elif option=="13" or option=="22":
    amount= budget - float(item13)
elif option=="17":
    amount= budget - float(item17)
elif option=="20":
    amount= budget - float(item20)
elif option=="21":
    amount= budget - float(item21)
elif option=="23":
    amount= budget- float(item23)

   
else:
    print("Invalid input")

vat= float('%.2f'%((amount)*0.05))
total=vat+amount
ran= random.randint(100,1000)
balance='%.2f'%(budget-total)

for x, y in menu.items():
        if option==x:
            print("You have selected", y)
            print("\n                                     CASH RECEIPT","\n\tReceipt number:",ran,"\n\tItem purchased:",y,"\n\t5% Vat:",vat,"\n\tTotal amount with 5% VAT:", total,"\n\tYour balance is:", balance,"AED","\n\tDate of purchase:", now,"\n")

    
print("Thank you for the purchase, please collect your item in the tray and balance through the output.")


