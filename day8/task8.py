'''def check(x):
    if x>= 50:
       return"passed"
    else:
        return"failed"
def grade(x):
    if x>90:
        print("The obtained grade is A")
    elif x>70 and x<90:
        print("The obtained grade is B")
    elif x>=50 and x<70:
        print("The obtained grade is C")
    else:
        print("The obtained grade is NG")


mark=int(input("Enter the marks: "))
try:
    check(mark)
except ValueError:
    print("Enter appropriate marks")
finally:
    grade(mark)
    '''


#------------------------------------------------------------#

#prepare a file to store the grade and scores of the student by calculating percentage and grade

def calc():
    phy=float(input("enter marks of physics: "))
    chem=float(input("enter marks of chemistry: "))
    math=float(input("enter marks of Mathematics: "))

    percent=(phy+chem+math)/3
    return phy,chem,math,percent

def calculate_grade(percent):
    if percent>90:
        return "A"
    elif percent>70 and percent<90:
        return "B"
    elif percent>=50 and percent<70:
        return "C"
    else:
        return "NG"
    
def main():
    name=input("Enter student's name: ")
    roll_no=int(input("Enter roll number: "))
    phy,chem,math,score=calc()
    with open("student_record.txt","a") as f:
        f.write(f"\n------RESULT------\n")
        f.write(f"Name: {name}\n")
        f.write(f"roll: {roll_no}\n")
        f.write(f"------Marks------\n")
        f.write( f"Physics: {phy}\n" )
        f.write( f"Chemistry: {chem}\n" )
        f.write( f"Mathematics: {math}\n" )
        f.write(f"Grade obtained: {calculate_grade(score)}\n")
        f.write(f"\nPercentage: {score:.2f}\n")

main()

