#ask user for input and put them in a list
'''count=0
inp_list=[]
asked=int(input("how many numbers you wanna enter?: "))
while count < asked:
    n=int(input("enter the number: "))
    inp_list.append(n)
    count+= 1
print(inp_list)'''

#a program to ask 5 numbers and perform the square of each number and store in another number
inp_list=[]
count=0
while count < 5:
    numbers=int(input("Enter the numbers: "))
    inp_list.append(numbers)
    count+= 1
print(f"The given list is {inp_list}")
square_list=[]
for i in inp_list:
    i=i**2
    square_list.append(i) 
print(f"The squared list of the numbers is {square_list}")
print(inp_list+square_list)




    