#Practice using conditional statements in Python.

#1.
'''If we run this Python code, what will be printed to the screen?
x = 10
y = '10'
if x == y:
    print('A')
else:
    print('B')
We proposed a few possible answers. Assign to a variable named correct the answer that you think is correct. For example, if you think that answer1 is correct, assign answer1 to correct.

answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Both A and B are printed.' '''

correct = answer3

#2.
''' If we run this Python code, what will be printed to the screen?
x = 10
y = '10'
if str(x) == str(y):
    print('A')
else:
    print('B')

answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Both A and B are printed.''''

correct = answer2	

#3.
'''If we run this Python code, what will be printed to the screen?
x = 3
y = 2
z = 1
if x > y:
    print('A')
if y > z:
    print('B')
if z > x:
    print('C')


answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Only C is printed.'
answer5 = 'Both A and B are printed.'
answer6 = 'Both A and C are printed.'
answer7 = 'Both B and C are printed.'
answer8 = 'All A, B and C are printed.''''

correct = answer5

#4.
'''If we run this Python code, what will be printed to the screen?
x = 3
y = 2
z = 1
if x > y:
    print('A')
elif y > z:
    print('B')
elif z > x:
    print('C')

answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Only C is printed.'
answer5 = 'Both A and B are printed.'
answer6 = 'Both A and C are printed.'
answer7 = 'Both B and C are printed.'
answer8 = 'All A, B and C are printed.''''

correct = answer2

#5.
'''If we run this Python code, what will be printed to the screen?
if True:
    print('A')
elif True:
    print('B')

answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Both A and B are printed.''''

correct = answer2

#6.
'''If we run this Python code, what will be printed to the screen?
if True and True:
    print('A')
if True and False:
    print('B')
if False and True:
    print('C')
if False and False:
    print('D')

answer1 = 'Only A is printed'
answer2 = 'Only D is not printed'
answer3 = 'Only B and C are printed''''

correct = answer1


#7.
'''If we run this Python code, what will be printed to the screen?
if True or True:
    print('A')
if True or False:
    print('B')
if False or True:
    print('C')
if False or False:
    print('D')

answer1 = 'Only A is printed'
answer2 = 'Only D is not printed'
answer3 = 'Only B and C are printed''''

correct = answer2

#8.
'''If we run this Python code, what will be printed to the screen?
if False or True and False:
    print('A')
if True or False and False:
    print('B')

answer1 = 'Nothing is printed.'
answer2 = 'Only A is printed.'
answer3 = 'Only B is printed.'
answer4 = 'Both A and B are printed.''''

correct = answer3

#9.
'''Write a program to count how many numbers bigger than 100 are in the values list. Assign the answer to a variable named num_bigger
values = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]'''

num_bigger = 0
for value in values:
    if value > 100:
        num_bigger += 1
#10.
'''Write a program to count how many even and odd numbers are in the values list. 
values = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]'''
num_even = 0
num_odd = 0

for value in values:
    if value%2 == 0:
        num_even += 1
    else:
        num_odd += 1

#11.
'''Write a program to check whether values1 is the reverse of values2. Assign the answer to a boolean variable named is_reversed. Both lists have the same length.
values1 = [80, 109, 111, 109, 94, 93, 108, 107, 81, 111, 101, 114, 102, 81, 107, 120, 108, 92, 113, 119, 97]
values2 = [97, 119, 113, 92, 108, 120, 107, 81, 102, 114, 110, 111, 81, 107, 108, 93, 94, 109, 111, 109, 80]'''

is_reversed = True
for i in range(len(values1)):
    if values1[i] != values2[-i - 1]:
        is_reversed = False

#12.
'''Write a program that creates a list named common that contains the characters that are common to both s1 and s2. The list of common characters should not contain duplicates, but it can have any order.

s1 = 'I have been busier these days due to having a lot on my plate.'
s2 = 'You have been very supportive towards my recent endeavors.' '''

common = [] 
for char in s1:
    if char in s2 and char not in common:
        common.append(char)

#13.
'''Write a program that calculates the maximum of the values list without using a built-in function. Assign the maximum value to a variable named maximum.
values = [72, 48, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15]'''

maximum = values[0]
for i in values:
    if i > maximum:
        maximum = i

#14.
'''Write a program that calculates the minimum of the values list without using a built-in function. Assign the minimum value to a variable named minimum.

values = [72, 48, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15]'''

minimum = values[0]
for i in values:
    if i < minimum:
        minimum = i
#15.
'''Given a list of numbers, find a pair of distinct values whose sum is equal to 100.
values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 10, 62, 48, 32, 96, 75, 15, 50, 50]'''

value1 = None
value2 = None
for x in values:
    for y in values:
        if x + y == 100 and x != y:
            value1 = x
            value2 = y

#16.
'''Given a list of numbers, find the number that appears the most.
values = [72, 50, 48, 50, 7, 66, 62, 32, 33, 75, 30, 85, 6, 85, 82, 88, 30, 32, 78, 39, 57, 96, 45, 57, 61, 32, 10, 62, 48, 32, 96, 75, 15]'''
most_frequent = values[0]
for value in values:
    if values.count(value) > values.count(most_frequent):
        most_frequent = value

print(most_frequent)        
    
#17.	
'''In this practice problem, you'll read the CSV file and count how many names have an estimated number greater than or equal to 100,000.
The data is contained the CSV file dq_unisex_names.csv'''
import csv
opened_file = open('dq_unisex_names.csv')
reader = csv.reader(opened_file)
all_rows = list(reader)

count = 0

for row in all_rows[1:]:
    if float(row[1]) >= 100000:
        count  += 1
        
        
print(count)

#18.
#In this problem, you'll create a new list containing only the rows where the length of the corresponding name is greater than ten.
opened_filed = open('dq_unisex_names.csv')
from csv import reader
read_file = reader(opened_filed)
all_data = list(read_file)

longest_names = []

for row in all_data[1:]:
    length  = len(row[0])
    if length > 10:
        longest_names.append(row[0])
        

        
for i in range(5):
    print(longest_names[i])

#19.
#In this practice problem, you'll need to find the most common unisex named. This means finding the name for which the estimated_number is the largest.

import csv
opened_file = open('dq_unisex_names.csv')
reader = csv.reader(opened_file)
all_rows = list(reader)

maximum = None
max_name = None
for row in rows[1:]:
    if maximum == None or float(row[1]) > maximum:
        maximum = float(row[1])
        max_name = row[0]

print(max_name)

#20.
#Let's calculate all names that have an estimated number of at most 1,000 people (inclusive).

import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_data = list(reader)

rare_names = []

for row in all_data[1:]:
    if float(row[1]) <= 1000:
        rare_names.append(row[0])
        
        
for i in range(5):
    print(rare_names[i])
    

'''





