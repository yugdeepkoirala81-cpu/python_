#truth table for and operator using python
print("Truth table for AND operator \n")
a= True
b= False
print(f"True AND True : {a and a}")
print(f"True AND False : {a and b}")
print(f"False AND True : {b and a}")
print(f"False AND False : {b and b}\n")
#truth table for or operator using python
print("Truth table for OR operator \n")
print(f"True OR True : {a or a}")
print(f"True OR False : {a or b}")
print(f"False OR True : {b or a}")
print(f"False OR False : {b or b}\n")
#truth table for not operator using python
print("Truth table for NOT operator \n")
print(f" NOT True : {not a}")
print(f" NOT False : {not b}")
#find out greater among a,b,c,d without using if-else
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
d=int(input("Enter fourth number "))
a_great=(a>b) and (a>c) and (a>d)
b_great=(b>a) and (b>c) and (b>d)
c_great=(c>a) and (c>b) and (c>d)
d_great=(d>a) and (d>b) and (d>c)
print(f"Is a the greatest number? : {a_great}")
print(f"Is b the greatest number? : {b_great}")
print(f"Is c the greatest number? : {c_great}")
print(f"Is d the greatest number? : {d_great}")









