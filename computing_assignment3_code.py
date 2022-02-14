#Saksham Beniwal
#EE
#21104076




#1 start

print('*****1 start*****')

text = str(input('enter a text: '))
text = text.lower() #lowers the text so that words like 'name' and 'NAME' will be considered equal

if ' ' not in text: #if there are no withespace, then it is single word, the following code is occurences for characters
    single_word = list(text) #creates a list of characters in the single word entered
    count_characters = {}

    for i in single_word:

        if i in count_characters:
            count_characters[i] = count_characters[i] + 1

        else:
            count_characters[i] = 1

    print('the occurence of each character in the word is: ')
    print(count_characters)

else: #case for multiple words, following code is for occurence of word

    multiple_words = text.split() #creates a list of words entered
    count_words = {}

    for j in multiple_words:
        
        if j in count_words:
            count_words[j] = count_words[j] + 1

        else:
            count_words[j] = 1

    print('the occurence of each word is: ')
    print(count_words)

print('*****1 end*****')
print()

#1 end




#2 start 

print('*****2 start*****')

year = int(input('enter a year within 1800 and 2025: '))

while year < 1800 or year > 2025:
    print('ERROR')
    year = int(input('enter a year within 1800 and 2025: '))

if year % 4 == 0 or year % 400 == 0:
    leap_year = True

    if year % 100 == 0 and year % 400 != 0:
        leap_year = False

else:
    leap_year = False

month = int(input('enter a month within 1 and 12: '))

while month < 1 or month > 12:
    print('ERROR')
    month = int(input('enter a month within 1 and 12: '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 9 or month == 11:
    days_length = 31

if month == 2:
    if leap_year == True:
        days_length = 29

    elif leap_year == False:
        days_length = 28

else:
    days_length = 30

days = int(input('enter a day within the limit: '))

while days < 1 or days > days_length:
    print('ERROR')
    days = int(input('enter a day within the limit: '))

if days < days_length:
    days = days + 1

elif days == days_length:
    days = 1
    
    if month == 12:
        month = 1
        year = year + 1

    else:
        month = month + 1

print('the next date is:', days, '/', month, '/', year)

print('*****2 end*****')
print() #adds a blank line

#2 end




#3 start 

print('*****3 start*****')

list_numbers = []
list_tuples_numbers = []

number = int(input('enter a number: '))

list_numbers.append(number) ##adds the number entered to list

resume = str(input('do you want to add more numbers(Y/N): '))

while resume != 'Y' and resume != 'N':
    print('ERROR')
    print('please enter Y or N')
    resume = str(input('do you want to add more numbers(Y/N): '))

while resume == 'Y':
    number = int(input('enter a number: '))

    list_numbers.append(number) #adds the number entered to list

    resume = str(input('do you want to add more numbers(Y/N): '))

    while resume != 'Y' and resume != 'N':
        print('please enter Y or N')
        resume = str(input('do you want to add more numbers(Y/N): '))

for i in list_numbers:

    list_tuples_numbers.append((i, i**2)) #adds tuples to list

print(list_tuples_numbers)

print('*****3 end*****')
print() #adds a blank line

#3 end




#4 start

print('*****4 start*****')

grade = int(input('enter a grade within 4 and 10: '))

while grade < 4 or grade > 10:
    print('ERROR')
    grade = int(input('enter a grade within 4 and 10: '))

if grade == 10:
    performance = 'outstanding'
    letter_grade = 'A+'

elif grade == 9:
    performance = 'excellent'
    letter_grade = 'A'

elif grade == 8:
    performance = 'very good'
    letter_grade = 'B+'

elif grade == 7:
    performance = 'good'
    letter_grade = 'B'

elif grade == 6:
    performance = 'average'
    letter_grade = 'C+'

elif grade == 5:
    performance = 'below average'
    letter_grade = 'C'

elif grade == 4:
    performance = 'poor'
    letter_grade = 'D'

print('your grade is', letter_grade, 'and', performance, 'performance')

print('*****4 end*****')
print() #adds a blank line

#4 end




#5 start

print('*****5 start*****')

pattern = 'ABCDEFGHIJK'

a = len(pattern)

for i in range(0, 6):

    print(pattern)

    text = list(pattern) #converts the pattern which is a string, to list, to make it editable and mutable

    text[a-i-1] = ' ' #adds whitespace
    text[a-i-2] = ' ' #adds whitespace

    for j in range(1,a):
        text[a-j] = text[a-j-1] #starting from last, one character before it is shifted to its position
        text[a-j-1] = ' '

    pattern = ''.join(text) #converts the list to string, to make it eligible for required result. I did not use 'for' loop for this, as the join function makes it more simple

print('*****5 end*****')
print() #adds a blank line

#5 end




#6 start

print('*****6 start*****')

student_details = {}

SID = int(input('enter the SID of the student: '))
name = str(input('enter the name of student: '))

student_details[SID] = name

resume = str(input('do you want to continue(Y/N): '))

while resume != 'Y' and resume != 'N':
    print('ERROR')
    print('please enter Y and N')
    resume = str(input('do you want to continue(Y/N): '))

while resume == 'Y':

    SID = int(input('enter the SID of the student: '))
    name = str(input('enter the name of student: '))

    student_details[SID] = name

    resume = str(input('do you want to continue(Y/N): '))

    while resume != 'Y' and resume != 'N':
        print('ERROR')
        print('please enter Y or N')
        resume = str(input('do you want to continue(Y/N): '))

#part a start
print(student_details) #answer for part a
#part a end

#part b start
print(sorted(student_details.values())) #answer for part b
#part b end

#part c start
print(sorted(student_details.keys())) #answer for part c
#part c end

#part d start
search = int(input("enter SID of student whom you want to search: "))
print(student_details[search]) #answer for part d
#part d end

print('*****6 end*****')
print() #adds a blank line

#6 end




#7 start

print('*****7 start*****')

terms = int(input('enter number of terms for fibonacci series: '))

a = 0 #first term
b = 1 #second term

print('the fibonaccin sequence is: ')
print (a)
print (b)

sum = a+b

for i in range(2,terms): #range starts from 2 as we have already printed the first 2 terms
    c = a+b
    sum = sum + c
    a = b
    b = c
    
    print(c)
print('the average of the fibonacci sequence is:', (sum/terms))

print('*****7 end*****')
print() #adds a blank line

#7 end




#8 start

print('*****8 start*****')

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#part a start
set_part_a_difference_12 = set1.difference(set2)
set_part_a_difference_21 = set2.difference(set1)

print('part a answer: ', set_part_a_difference_12.union(set_part_a_difference_21))
#part a end

#part b start
set_part_b_intersection_12 = set1.intersection(set2)
set_part_b_intersection_13 = set1.intersection(set3)
set_part_b_total_union = set1.union(set2, set3)

print('part b answer: ', set_part_b_total_union.difference(set_part_b_intersection_12, set_part_b_intersection_13))
#part b end

#part c start
set_part_c_intersection_12 = set1.intersection(set2)
set_part_c_intersection_13 = set1.intersection(set3)

print('part c answer: ', set_part_c_intersection_12.union(set_part_c_intersection_13))
#part c end

#part d start
print('part d answer :', set.difference(set1))
#part d end

#part e start
set_part_e_total_union = set1.union(set2, set3)

print('part e answer: ', set.difference(set_part_e_total_union))
#part e end


print('*****8 end*****')
print() #adds a blank line

#8 end