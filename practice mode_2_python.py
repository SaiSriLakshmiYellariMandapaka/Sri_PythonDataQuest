#Practice working with variables and doing calculations with variables.
#1.
'''Create a variable gpa and assign it the value of Alice's GPA using the information contained in the following table:
Course 	      Grade   Hours
Mathematics 	4 	4
History 	3 	2
Science 	4 	3
Art     	2 	2
English 	3 	3'''

grade_hours = 4*4+3*2+4*3+2*2+3*3
no_of_hours = 4+2+3+2+3
gpa = grade_hours/no_of_hours

#2.
#Assign a string of length 128 that contains 128 times the character * to a variable named stars.

# solution 1:
stars = '*'
stars += stars
stars += stars
stars += stars
stars += stars
stars += stars
stars += stars
stars += stars

# solution 2:
stars = '*' * 128

#3.
'''A variable named seconds has already been defined and contains the total number of seconds elapsed in the day so far.

    Assign to a variable named hour the current hour of the day.
    Assign to a variable named minute the current minute of the day.'''

seconds = 48600
hour = int(seconds / 3600)
minute = int((seconds - 3600 * hour) / 60)

#4.
'''Define variables named john, bob and alice and assign to each of them the body mass index of the person based on the information contained on the table above.
Name 	Weight (in kilograms) 	Height (in meters)
John 	67 	1.82
Bob 	80 	1.79
Alice 	50 	1.55'''

john = 67/(1.82**2)
bob = 80/(1.79**2)
alice = 50/(1.55**2)

#5.
#A float variable x has been defined with some value.Create a variable named decimal and assign to it the decimal part of x.

# variable x is available to you
decimal = x - int(x)

#6.
'''Two variables named number_of_apples and numbers_of_persons have been defined, representing the total number of apples and the total number of people you want to give apples.

    Create a variable named apples_given_to_each and assign it the number of apples that each person will get.
    Create a variable named apples_left and assign to it the number of apples left in the end.

Remember, you give the same number of apples to each person and do not cut any apples.'''

number_of_apples = 12345
numbers_of_persons = 3517

apples_given_to_each = int(number_of_apples/numbers_of_persons)
apples_left =  number_of_apples - apples_given_to_each* numbers_of_persons

#7.
'''We propose a few possible answers. Assign to a variable named correct the answer that you think is the right one. For example, if you think that answer1 is the correct answer, assign answer1 to `correct.

What will be the values of x and y after executing the following code:

x = 1

y = 2

x = y

y = x

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2''''

correct = answer4

#8.
'''We propose a few possible answers. Assign to a variable named correct the answer that you think is the right one. For example, if you think that answer1 is the correct answer, assign answer1 to `correct.

What will be the values of x and y after executing the following code:
x = 1
y = 2
tmp = x
x = y
y = tmp

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2' '''

correct = answer3

#9.
'''We propose a few possible answers. Assign to a variable named correct the answer that you think is the right one. For example, if you think that answer1 is the correct answer, assign answer1 to `correct.

What will be the values of x and y after executing the following code:
x = 1
y = 2
total = x + y
x = total - x
y = total - y

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2' '''

correct = answer3

#10
'''We propose a few possible answers. Assign to a variable named correct the answer that you think is the right one. For example, if you think that answer1 is the correct answer, assign answer1 to `correct.

What will be the values of x and y after executing the following code:
x = 1
y = 2
x = x + y
y = x - y
x = x - y

answer1 = 'x = 1 and y = 2'
answer2 = 'x = 1 and y = 1'
answer3 = 'x = 2 and y = 1'
answer4 = 'x = 2 and y = 2' '''

correct = answer3


