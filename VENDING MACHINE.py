


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
menu2= Menu("2  ","Pringles- BBQ Flavor     ", "6.50 AED")
menu3= Menu("3  ","Lays- Salt and Vinegar   ", "1.75 AED")

menu4= Menu("4  ","Snickers                 ", "3 AED")
menu5= Menu("5  ","Mars                     ", "2.50 AED")
menu6= Menu("6  ","Kitkat                   ", "2 AED")
menu7= Menu("7  ","Toblerone                ", "5.75 AED")

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


        



