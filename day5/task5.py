queue=int(input("How many student data do you want to enter?: "))
std_list={}
while queue>0:
    queue-=1
    inp_name=input("Enter Name: ")
    inp_class=int(input("Enter class: "))
    std_list[inp_name] = inp_class
print(std_list)