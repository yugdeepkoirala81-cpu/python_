#same program as de2task.py but use different assignment operators

import math
#to calculate total bill to be paid of several units of items after dedecting discouunt and adding tax
import math
print("Discount for all items is 10% ")
print("Tax for all items is 13% ")
uni=int(input("Enter number of units purchased: "))
pri=float(input("Enter price per unit: "))
total=uni*pri
total-=(total*0.10) #applying discount using -= operator
total+=(total*0.13)     #adding tax using += operator
fin=float(total) #final amount
print(f"Total bill to be paid after discount and adding tax is: {fin:.3f}")
