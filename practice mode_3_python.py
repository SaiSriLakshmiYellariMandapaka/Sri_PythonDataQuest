#Practice using Python lists and for loops.

#1.
'''Print all sentences contained in the lines list, one per line.
lines = ["My candle burns at both ends;", "It will not last the night;", "But ah, my foes, and oh, my friends —", "It gives a lovely light."]'''

for i in lines:
    print(i)

#2.
#We declared a variable N for you. N = 11.Your task is to print all values from 0 to N (inclusive).

for i in range(N+1):
    print(i)

#3.
#Your task is to print all numbers from 42 to 59 (inclusive).

for i in range(42,60):
    print(i)   

#4.
#Increase by one each value contained in the values list.values = [16, 1, 7, 2, 19, 12, 5, 20, 2, 10, 10, 14, 17, 14, 1, 16, 19, 7, 9, 19]


for i in range(len(values)):
    values[i]+=1

print(values)

#5.
'''We provide a list of values in the values variable.
 Define a reversed_values variable whose values are the values in the values list, but in reversed order.'''

reversed_values = []
for i in range(len(values)):
    reversed_values.append(values[len(values) -i -1])
      
print(reversed_values)

#6.
'''Define a variable answer and assign to it the value that values_copy will have after executing the above code.
What will be the value of values_copy after we execute the following code:

values = [5, 4, 7, 8, 9, 3]
values_copy = []
for v in values:
    values_copy = v'''

answer = 3

#7.
'''Define a variable answer_x and assign to it the value that x will have after executing the above code.
Define a variable answer_total and assign to it the value that total will have after executing the above code.
What will be the values of x and total after we execute the following code:

values = [3, 5, 2, 1]

total = 0
for x in values:
    total += x'''

answer_x = 1
answer_total =11

#8.
'''Define a variable answer and assign to it the value that x will have after executing the above code.
What will be the value of x after we execute the following code:

values = [3, 5, 2, 1]

for x in values:
    x = 0'''

answer = 0

#9.
'''Define a variable answer_x and assign to it the value that x will have after executing the above code.
Define a variable answer_total and assign to it the value that total will have after executing the above code.

What will be the values of x and total after we execute the following code:

values = [3, 5, 2, 1]
total = 0
for x in values:
    total = x'''

answer_x = 1
answer_total = 1

#10.
'''Define a variable answer and assign to it the number of values that will be printed if we execute the above code.
How many values will be printed if we execute the following code:
for i in range(10):
    print(i)
    i = 11'''
answer = 10

#11.
'''Define a variable answer and assign to it the value that values_copy will have after executing the above code
What will be the value of values_copy after we execute the following code:

values = [5, 4, 7, 8, 9, 3]
values_copy = []
for v in values:
    values_copy.append(v)'''

answer = [5, 4, 7, 8, 9, 3]

#12.
#Write a Python program that creates a list of lists named matrix_of_ones that represents a 7 by 3 matrix where each number is equal to 1.

matrix_of_ones = [
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1],
    [ 1, 1, 1]]

#13.
'''Write a Python program that calculates the number of rows and columns of the matrix stored in variable matrix.
Assign the number of rows to a variable named num_rows and the number of columns to a variable named num_cols.

matrix = [
    [0, 9, 5, 4, 5, 3, 1, 5, 7],
    [8, 2, 1, 7, 3, 1, 5, 7, 0],
    [1, 5, 3, 2, 7, 1, 4, 4, 8],
    [2, 5, 6, 2, 0, 4, 1, 9, 3],
    [7, 4, 2, 9, 7, 0, 7, 4, 4]]'''

num_rows = len(matrix)
num_cols = len(matrix[0])

#14.
'''Write a Python program that sums all values in the matrix stored in variable matrix. Assign the result to a variable named total.
matrix = [
    [0, 9, 5, 4],
    [8, 2, 3, 0],
    [1, 5, 3, 2]]'''

num_rows = len(matrix)
num_cols = len(matrix[0])

total = 0
for row in range(num_rows):
    for col in range(num_cols):
        total+=matrix[row][col]

#15.
'''Write a Python program that calculates the average of the values list. Assign the result to a variable named average.
values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]'''

for i in values:
    average = sum(values)/len(values)

#16.
'''Create a list named word_len whose elements are the lengths of the words in words. The first element should be the length of the first word; the second element is the length of the second word, and so on.
words = ['tissue', 'psychology', 'blind', 'assessment', 'dynamic', 'hero', 'circulation', 'merchant', 'publication', 'interference', 'show', 'joy', 'sour', 'aloof', 'grass', 'distortion', 'exclude', 'pressure', 'bullet', 'calf']'''

word_len = []
for word in words:
    word_len.append(len(word))

#17.
#Print all characters of sentence, one character per line.sentence = 'I\'m practicing printing string characters!'

for c in sentence:
    print(c)

#18.
'''
    Import the csv module.
    Use the open command to read the CSV file dq_unisex_names.csv.
    Assign the header row to a variable named headers.
    Assign the data rows to a variable named rows (do not include the header row).

Optional steps to test your answer:

    Print the value of header to check it contains the correct headers.
    Print the first five rows in rows to see if they match the table.'''

import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
headers = all_rows[0]
rows = all_rows[1:]

# Testing answer

print(headers)
for i in range(5):
    print(rows[i])

#19.
'''
    Import the csv module.
    Use the open command to read the CSV file dq_unisex_names.csv.
    Assign the data rows to a variable named rows (do not include the header row).
    For each row in rows, append to it the length of the name contained in that row.

Optional steps to test your answer:

    Print the first five data rows to see if they match the table example above.'''

import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)
rows = all_rows[1:]
for row in rows:
    name = row[0]
    row.append(len(name))
    
# Testing answer

for i in range(5):
    print(rows[i])

#20.
'''
    Import the csv module.
    Use the open command to read the CSV file dq_unisex_names.csv.
    Assign the data rows to a variable named rows (do not include the header row).
    For each row in rows, convert the value on the estimated number column from string to float.

Optional steps to test your answer:

    Print the first five data rows to see if they match the table example above.
    Using the type() function, print the data type of the estimated number column in the first data row.'''

import csv
file = open('dq_unisex_names.csv')
reader = csv.reader(file)
all_rows = list(reader)

rows = all_rows[1:]
for row in rows:
    row[1] = float(row[1])
    
for i in range(5):
    print(rows[i])

print(type(row[0][1]))    









