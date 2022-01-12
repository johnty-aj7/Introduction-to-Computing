# Assignment 1

#Q1

#input
n1= int(input("Enter 1st no. :"))
n2= int(input("Enter 2nd no. :"))
n3= int(input("Enter 3rd no. :"))

#formula
avg = (n1 + n2 + n3)/3

print("Avg :",avg)

print("\n")

#Q2

#input

grossIncome= float(input("Gross income to the nearest penny :"))
dependents= int(input("Number of dependents :"))

taxableIncome = grossIncome - 10000 - (3000*dependents)
tax = (taxableIncome*20)/100

if tax<0:
    print("Income tax is 0$")
else:
    print("tax :",tax)


print("\n")

#Q3

#input

SID = int(input("SID :"))
name = input("name :")
gender = input("Gender :")
course = input("Course name :")
cgpa = float(input("CGPA :"))

#list

Student = [SID,name,gender,course,cgpa]

print("Student",Student)



print("\n")

#Q4

#input

m1=float(input("marks in sub 1 :"))
m2=float(input("marks in sub 2 :"))
m3=float(input("marks in sub 3 :"))
m4=float(input("marks in sub 4 :"))
m5=float(input("marks in sub 5 :"))


#list

Marks = [m1,m2,m3,m4,m5]
Marks.sort()
print("Marks :",Marks)


print("\n")

#Q5
#a)
color= ['red' , 'green' , 'white' ,'black', 'pink' , 'yellow']
color.remove('black')
print(color)

print("\n")
#b)

color=['red' , 'green' , 'white' ,'black', 'pink' , 'yellow']
color[3:5]=["Purple"]
print(color)

#  Thank You
