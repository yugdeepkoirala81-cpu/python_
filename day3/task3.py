#question 1
dest=input("Enter the destination: ") .lower()
price=int(input("Enter the price: "))
max_price=50000
book= price<=max_price and (not dest=="asia" ) 
print(f"Should I book the ticket: {book}")

#question 2
approved_ids=["A101", "B205", "C303", "0410"]
employee_id=input("Enter your employee ID: ").upper()
check=employee_id in approved_ids
print(f"the id is among the employees?: {check}")
print("The next id to be checked is Z9999")
usercheck= "Z9999" not in approved_ids
print(f"Z9999 is not among the employees?: {usercheck}")

#question 3
balance=1000
deposit=250
service_fee=10.50
interest=1.05
balance+= 250
balance-= 10.50
balance*=1.05
final_balance=balance 
print(f"Final account balance: {final_balance:.3f}")
balance//=100
print(f"Approximate number of shares that can be bought: {balance}")