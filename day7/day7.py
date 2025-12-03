#args and kwargs
'''
def func(*arg):
    print(f"The arg are {arg[0]}")
    print(f"The arg are {arg[1]}")
    print(f"The arg are {arg[2]}")

func(1021,"nig",21)'''

'''def cles(*arg):
    sum=0
    for i in arg:
        sum=sum+i
    print(sum)

cles()
cles(12,11)
cles(123,121,22)
cles(11,10,15,13,9,7)'''

'''def function(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

function(name="Ulla", place="brt", religion="muhammed", Class= 11)''' 

def my_func(*arg,**kwarg):
    for i in arg:
        print(i)
    for i,j in kwarg.items():
        print(f"{i}:{j}")

my_func("Yugdeep", city="brt", state="koshi", country="nepal")