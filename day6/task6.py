def check(x):
    if x>= 50:
       return"passed"
    else:
        return"failed"
def grade(x):
    if x>90:
        print("The obtained grade is A")
    elif x>70 and check(x)<90:
        print("The obtained grade is B")
    else:
        print("The obtained grade is C")

def main():
    mark=int(input("Enter the marks: "))
    call=check(mark)
    print(f"The student has {call} the exam")
    if check(mark) == "pass":
        grade(mark) 
    else:
        print("NG, Get better")

main()

    


