#Saksham Beniwal
#EE
#21104076




#1 start

print('*****1 start*****')

def text(a, start, end):
    print('move disc', a, 'from rod', start, 'to rod', end)

def tower_of_hanoi(n, start_rod, end_rod):

    if n == 1:
        text(n, start_rod, end_rod)

    else:
        temporary_rod = 6 - (start_rod + end_rod) #gives the value of rod other than that of start rod and end rod
        tower_of_hanoi(n - 1, start_rod, temporary_rod)
        text(n, start_rod, end_rod)
        tower_of_hanoi(n - 1, temporary_rod, end_rod)

tower_of_hanoi(3, 1, 3) #solves tower of hanoi for 3 disc moving from first rod to third rod

print('*****1 end*****')
print()

#1 end




#2 start

print('*****2 start*****')

#recursive method start
def pascal_triangle(n): #gives a list that contains many list containing values held by a pascal triangle

    if n == 1:
        return [[1]]

    else:
        new_row = [1]
        result = pascal_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row += [1]
        result.append(new_row)
        return result

rows = int(input("Enter the number of rows you want(greater than 0): "))

while rows < 1:

    print('ERROR')
    print('enter a number greater than 0')
    rows = int(input('Enter the number of rows you want(greater than 0): '))

triangle = pascal_triangle(rows)
width = len(str(triangle[-1])) - 2

print('pascal triangle for recursive method is: ')

#the below code adds spaces in between values and prints it in triangle form
for i in triangle:
    spaces = ""

    for j in i:
        spaces += (f"{j}" + "   ") 

    print(spaces.center(width * 2, " "))
#recursive method end

#iterative method start
rows = int(input("Enter the number of rows you want(greater than 0): "))

while rows < 1:

    print('ERROR')
    print('enter a number greater than 0')
    rows = int(input('Enter the number of rows you want(greater than 0): '))

triangle = [[1]]

#the below code gives a list that contains many list containing values held by a pascal triangle
while len(triangle) < rows:

    new_row = [1]
    last_row = triangle[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    triangle.append(new_row)

width = len(str(triangle[-1])) - 2

print('pascal triangle for iterative method is: ')

#the below code adds spaces in between values and prints it in triangle form
for i in triangle:
    spaces = ""

    for j in i:
        spaces += (f"{j}" + "   ")

    print(spaces.center(width * 2, " "))
#iterative method end

print('*****2 end*****')
print() #adds a blank line

#2 end





#3 start

print('****3 start*****')

num_1 = int(input('enter first number: '))
num_2 = int(input('enter second number: '))

division_12 = divmod(num_1, num_2) #returns tuple whose first value is quotient and second value is remainder
division_21 = divmod(num_2, num_1) #function used is divmod()

print('quotient when first number is divided by second number is:', division_12[0])
print('quotient when second number is divided by first number is:', division_21[0])

print('remainder when first number is divided by second number is:', division_12[1])
print('remainder when second number is divided by first number is:', division_12[1])

#part a start
#function used is callable()
print('value of variable division_12 is callable:', callable(division_12))
print('value of variable division_12 is callable:', callable(division_21))
print('value of function divmod for both divisions is callable:', callable(divmod))
#part a end

#part b start
#function used is index() and append()
values_list = []

values_list.append(division_12[0])
values_list.append(division_21[0])
values_list.append(division_12[1])
values_list.append(division_21[1])

if values_list.index(0) == True:
    print('all the values are NOT non-zero')

else:
    print('all the values are non-zero')
#part b end

#part c start
#function used is append()
values_list.append(4)
values_list.append(5)
values_list.append(6)

filtered_values = []

for j in values_list:

    if values_list[j] > 4:
        filtered_values.append(values_list[j])

print('the filtered out values are:')

for k in filtered_values:
    
    print(k)
#part c end

#part d starts
#functions used is set()
set_filtered_values = set(filtered_values)

print('the set of filtered out result is:', set_filtered_values)
#part d ends

#part e starts
#function used is frozenset()
immutable_set_filtered_values = frozenset(set_filtered_values)

print('the immutable version of set of filtered out values is:', immutable_set_filtered_values)
#part e ends

#part f starts
#function used is set()
maximum_value = max(set_filtered_values)

print('the maximum value in set is:', maximum_value)
print('the hash value of the maximum value is:', hash(maximum_value))
#part f ends

print('*****3 end*****')
print() #adds a blank line

#3 end





#4 start

print('*****4 start*****')

class student:

    def __init__(my, name, roll_number): #uses __init__() function to assign 'name' and 'roll number' to objects
                                         #'my' parameter is used as reference 
        my.name = name
        my.roll_number = roll_number

    def student_data(my): #function for assigning values

        print('Name:', my.name)
        print('Roll Number:', my.roll_number)
        print()

    def __del__(my): #uses __del__() to delete objects

        print('the object is deleted:', my.name, ',', my.roll_number)

data_1 = student('Pratyush Soni', 21104043)
data_2 = student('Saksham Beniwal', 21104076)
data_3 = student('Manobal Singh Bagady', 21104129)

data_1.student_data()
data_2.student_data()
data_3.student_data()

del data_2

print('*****4 end*****')
print() #adds a blank line

#4 end





#5 start

print('*****5 start*****')

class employee_data:

    def __init__(personal, name, salary): #assigning 'name' and 'salary' to objects
                                          #'personal' parameter is reference

        personal.name = name
        personal.salary = salary

    def employee_data(personal): #function for assigning values

        print(personal.name, '              ', personal.salary) #space is given to emulate table form

employee_1 = employee_data('Mehak', 40000)
employee_2 = employee_data('Ashok', 50000)
employee_3 = employee_data('Viren', 60000)

print('Name                 Salary') #space is given to emulate table form
print('---------------------------')

employee_1.employee_data()
employee_2.employee_data()
employee_3.employee_data()

#part a start
employee_1.salary = 70000 #updates salary of Mehak

print('After updating salary of Mehak:')

print('Name                 Salary') #space is given to emulate table form
print('---------------------------')

employee_1.employee_data()
employee_2.employee_data()
employee_3.employee_data()
#part a end

#part b start
del employee_3 #deletes for Viren

print('After deleting the record of Viren:')

print('Name                 Salary') #space is given to emulate table form
print('---------------------------')

employee_1.employee_data()
employee_2.employee_data()
#part b end

print('*****5 end*****')
print() #adds a blank line

#5 end





#6 start
#since questions says only code, so I am not writing any comments

print('*****6 start*****')

word_george = str(input('enter the word said by George: '))
word_barbie = str(input('enter the word arranged by Barbie: '))

word_george = word_george.lower() 
word_barbie = word_barbie.lower()

list_word_george = list(word_george)
list_word_barbie = list(word_barbie)

list_word_george.sort()
list_word_barbie.sort()

if list_word_george != list_word_barbie:

    print('friendship is FAKE')

elif list_word_george == list_word_barbie:

    print('friendship is TRUE')

print('*****6 end*****')
print()

#6 end
