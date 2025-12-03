std_marks=float(input("Enter the marks of the student: "))
check= std_marks>=50
if check==False:
    print(f"The student has failed ")
elif check==True:
    print(f"The student has passed")
    if std_marks>=90:
        print(f"The student has obtained A grade")
    elif std_marks>=80 and std_marks<90:
        print("The student has obtained B grade")
    elif std_marks>=70 and std_marks<80:
        print("The student has obtained C grade")
    else:
        print("The student has obtained D grade")
else:
    print("Enter a valid mark")