name=input("enter your name:")
dob=input("enter your year of birth(DD/MM/YYYY):")
reg_no=input("enter your register number:")
department=input("enter your department:")
mark1=input("enter your sub 1 marks:")
mark2=input("enter your sub 2 marks:")
mark3=input("enter your sub 3 marks:")
mark4=input("enter your sub 4 marks:")
mark5=input("enter your sub 5 marks:")
total=mark1+mark2+mark3+mark4+mark5
average=total / 5
print("\n stdent details:\n")
print("Name",name)
print("DOB",dob)
print("Register number",reg_no)
print("Department",department)
print("total marks",total)
print("average marks",average)
if average>=90:
    print("Excellent")
elif average>=75:
    print("very good")
elif average>=60:
    print("good")
elif average>=50:
    print("pass")
else:
    print("fail")
        
