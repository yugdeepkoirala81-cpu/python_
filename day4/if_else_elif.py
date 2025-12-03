# to check whether the number is positive, negative or zero
num=int(input("enter a number: "))
if num>0:
   print(f"{num} is positive")
elif num<0:
 print(f"{num} is negative")
else:
 print(f"{num} is zero")

#to check larger among 3 numbers
a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
if a>=b>=c:
    print(a," is greatest")
elif b>=c:
    print(b," is greatest")
else:
    print(c, " is greatest")