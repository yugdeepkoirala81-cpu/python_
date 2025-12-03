#creating a file

'''file_path="test.txt"
f=open(file_path,"x") 
print(f.name)
print(f.mode)'''

#writing in a file

'''f=open("test.txt","w")
f.write(f"Wssp wssp twin \n")
f.write(f"Hope you good gng")
f.close()
'''

#reading the file

'''f=open("test.txt","r")
# data=f.read()
line1=f.readline()
line2=f.readline()
print(line1)
print(line2)
f.close()'''

#This is traditional way. Nowadays new way is used to perform file handling by the help of "with" keyword
#-------------------------------------------------#




'''with open("test.txt","r") as f:
    content = f.read()
    print(content)'''

#To append something

'''with open("test.txt","a")as f:
    f.write("\nThis is recently added content")
'''
with open("test.txt","r")as f:
        content=f.read()
with open("copy.txt","a")as x:
    x.write(f"{content}")



