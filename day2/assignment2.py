#return false value if the user inputs default value such as 12345678 or password
passw=input("Enter your password: ")
defp = "12345678"
min_len=8
max_len=20
max_check=len(passw) < max_len
leng=len(passw)>=min_len
chek = (passw!=defp)
print(f" is it meeting the minimum length requirement? : {leng}")
print(f"is it something other than the default password? : {chek} ")
print(f"is it below the max lenght? : {max_check}")

