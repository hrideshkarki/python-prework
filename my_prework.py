# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("hello_"+username.upper()+"!")
username=input("Please enter your username:")
hello_name('username')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for value in range (1, 101):
        if value%2==1:
            print(value)
        else:
            value+=1
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has 
# been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    print(max(list))
list=[1, 2, 3, 4, 22]
max_num_in_list(list)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    if year%400==0:
        print(str(year)+" is a leap year.")
    elif a_year%100==0:
        print(str(year)+" is a not leap year.")
    elif a_year%4==0:
        print(str(year)+" is a leap year.")
    else:
        print(str(year)+" is a not leap year.")
year=int(input("Please enter a year:"))
is_leap_year(year)


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are 
# consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):


def is_consecutive(a_list):
    if a_list==list(range(min(a_list),max(a_list)+1)):
        print("True")
    else:
        print("False") 
list1=[1, 2, 3, 4, 5]
is_consecutive(list1)