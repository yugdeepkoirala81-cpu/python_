# a program to ask two numbers from user and perform division operation
try:
    num1=int(input("enter number: "))
    num2=int(input("enter another number: "))
    div=float(num1/num2)
except ValueError :
    print("Value error occured")
except TypeError:
    print("type error occured")
except ZeroDivisionError:
    print("Zero div occured")
else:
    print(f"{div:.3f}")
finally:
    print("program performed")
