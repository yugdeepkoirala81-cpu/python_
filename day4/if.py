a=17
if a > 10:
    print("a is greater than 10")

#ask user for input and execute the block only if the name entered is your name
nem=input("Enter your name: ").lower()
if nem:
    if nem=="yugdeep":
        print("Welcome Yugdeep!")
#ask user amt to be paid and if amt is >1000 compute the discount of 10% and calculate the actual amt to be paid otherwise just print the amt
amt=float(input("Enter the amount to be paid: "))
greater=amt>1000
if greater==True:
    discount=amt*0.10
    actual_amt=amt-discount
    print(f"Amount to be paid after discount: {actual_amt:.2f}") 
if greater==False:
    print(f"Amount to be paid: {amt:.2f}")

    