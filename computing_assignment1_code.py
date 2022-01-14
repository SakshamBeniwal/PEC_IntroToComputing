#1
num_1 = int(input('enter first number: '))
num_2 = int(input('enter second number: '))
num_3 = int(input('enter third number: '))

avg = ((num_1+num_2+num_3)/3)

print('the average of the three numbers entered is: ', avg)
print() #adds a blank line




#2
gross_income = int(input('enter your gross income: '))
dependent = int(input('enter no. of dependents: '))
standard_deduction = 10000
dependent_deduction = 3000
tax_rate = 0.2 #20%=0.2

taxable_income = gross_income-standard_deduction-(dependent_deduction*dependent)
tax = taxable_income*tax_rate

if tax <= 0:
    tax = 0
    print('your income tax is: ', tax)
    
else:
    print('your income tax is: ', tax)
print() #adds a blank line




#3
SID = int(input('enter your SID: '))
name = str(input('enter your name: '))
gender = str(input('enter your gender(M, F, U): '))
course = str(input('enter your course name: '))
CGPA = float(input('enter your CGPA: '))

student_data = [SID, name, gender, course, CGPA]

print(student_data)
print() #adds a blank line




#4
marks_1 = int(input('enter marks of first student: '))
marks_2 = int(input('enter marks of second student: '))
marks_3 = int(input('enter marks of third student: '))
marks_4 = int(input('enter marks of fourth student: '))
marks_5 = int(input('enter marks of fifth student: '))

marks = [marks_1, marks_2, marks_3, marks_4, marks_5]
print(marks)

marks.sort()

print('list after sorting: ', marks)
print() #adds a blank line




#5 part a
color = ['red', 'green', 'white', 'black', 'pink', 'yellow']

del color[3]

print('new list after deleting fourth item: ', color)




#5 part b
color = ['red', 'green', 'white', 'black', 'pink', 'yellow']

color[3] = color[4] = 'purple'

print('new list after replacing black and pink with purple: ', color)
print() #adds a blank line



        

    
