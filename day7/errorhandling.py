'''s=int("")

print(s)
'''

'''a=45
b='123'
print(a+b)
'''

'''a=76
b=0
print(a/b) '''

try: #place risky code
    s=int("hello")
    print(s)
    print(type(s))
except: # run back statement
   print("exception occured")
finally: #runs code anyhow
      print("code ended")

