#ask user to input password and if password length is less than 4 print add more chracters
passw=input("Enter your password: ")
if len(passw)<4:
    print("Add more characters to your password")   
else:
    print("Password accepted")
    
print("Length of your password is:", len(passw))

