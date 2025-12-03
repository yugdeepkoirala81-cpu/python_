#functions
'''def area(l,b):
    area=l*b
    return(area) 
x=int(input("enter length: "))
y=int(input("enter breadth: "))
print(f"area is {area(x,y)} ")'''
#parameters are the input of the functions in the executional block

'''def sec_fnc(nme,age): #parameters
    print(f"hello {nme} YOU re of {age} age")

inp_nm=input("enter name: ")
inp_ag=int(input("enter age: "))
sec_fnc(inp_nm,inp_ag) #arguments   '''

# ''def sum(x,y):
#     return x + y
# def dif(x=10,y=5):   #default parameters; only takes such value if no input is given and if 
#     #more than one values are given , the first parameter shouldnt be made default
#     return x - y 

# a=int(input("enter nu.: "))
# b=int(input("enter num "))
# print(f'''   sum of  {a} and {b} is {sum(a,b)}
#     difference  is {dif()}  ''')   ''

'''
def operations(x,y):
    return x+y, x-y,x*y,x/y

result=operations(10,5)
print(result)
sm,dif,pro,div=result
print(sm)
print(dif)
print(pro)
print(div)'''

def list_len(list1):
    # print(len(list1))
    for i in list1:
        print(i)
list_len(["ihi",23])


