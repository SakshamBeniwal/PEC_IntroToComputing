#Saksham Beniwal
#EE
#21104076




#1 start
given_text = 'Python is a case sensitive language'

#part a
print('length of the given string is:', len(given_text))

#part b
print('the reverse order of the given string is:', given_text[-1::-1]) #slicing starts from last word and moves one by one to first, so we get a reverse order

#part c
print('the required sliced portion of the given string is:', given_text[10:26])

#part d
print('the required string with replaced part is:', given_text.replace('a case sensitive', 'object oriented'))

#part e
print('the index of a in given string is:', given_text.find('a'))

#part f
print('the string with no whitespace is:', given_text.strip())

print() #adds a blank line
#1 end




#2 start
Name = 'Saksham Beniwal'
SID = '21104076'
Department_Name = 'Electrical Engineering'
CGPA = '10.0'

print('''Hey, {} Here!
My SID is {}
I am from {} department and my CGPA is {}'''.format(Name, SID, Department_Name, CGPA))

print() #adds a blank line
#2 end




#3 start
a = 56
b = 10

#part a
print('a&b=', a&b)

#part b
print('a|b=', a|b)

#part c
print('a^b=', a^b)

#part d
print('a<<2=', a<<2, 'b<<2=', b<<2)

#part e
print('a>>2=', a>>2, 'b>>4=', b>>4)

print() #adds a blank line
#3 end




#4 start
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
num3 = int(input('enter third number: '))

num = [num1, num2, num3]

print('the greatest of the three numbers entered is:', max(num))

print() #adds a blank line
#4 end




#5 start
text = str(input('enter a text: '))
text = text.lower() #this has been done so that words like 'Name' and 'NAME' can also be detected as python is a case sensitive language

if 'name' not in text:
    print('no')
else:
    print('yes')

print() #adds a blank line
#5 end




#6 start
length_1 = int(input('enter the length of first side: '))
length_2 = int(input('enter the length of second side: '))
length_3 = int(input('enter the length of third side: '))

length = [length_1, length_2, length_3]
length.sort() #sorts length in ascending order

if length[2] >= (length[0] + length[1]):
    print('no')
else:
    print('yes')

    #we have considered only one case because length[0] and length[1] will be smaller than length[2] (as they are arranged in ascending order)
    #hence there is no possibility that either of length[0] or length[1] will be greater then sum of other two

print() #adds a blank line
#6 end
    


 




