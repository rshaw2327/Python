start=50
while(start!=0):
    if(start//10==3 or start%10==3):
        print(start,end=" ")
    start=start-1  

count = 0
number = 1

while number <= 100:
    if number % 5 == 0:
        count += 1
    number += 1

print("Total count of numbers divisible by 5 from 1 to 100:", count)

number = input("Enter a number: ")

# Reverse the number using slicing
reversed_number = number[::-1]

# Check if the original number is the same as the reversed number
if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# Input the value of N from the user
N = int(input("Enter the value of N: "))
# Initialize variables
sum_of_squares = 0
number = 1

# Calculate the sum of squares using a while loop
while number <= N:
    sum_of_squares += number ** 2
    number += 1

# Print the result
print(f"The sum of the squares of the first {N} natural numbers is: {sum_of_squares}")

for i in range (2,101,2):
    print(i, end=" ")

import calendar
for i in range(2000,2100):
    is_leap = (calendar.isleap(i))
    if is_leap == True:
        print(i, end=" ")
    

def factorial (number):
    factorial=1
    for i in range(number,0,-1):
        factorial=factorial*i   
    print(factorial)           
number=int(input("please enter the number"))    
factorial(number)



count=0
num=2

while(count<10):
    factors=0
    for i in range(1,num+1):
        if (num%i==0):
            factors=factors+1
    if (factors==2):
        count=count+1
        print(num,end= " ")
    num=num+1

def prime_number(starting_num,ending_num):
    
    for i in range(starting_num,ending_num+1):
        factors=0
        for j in range(1,i+1):
            if(i%j==0):
                factors=factors+1
        if(factors==2):
            print(i)        
starting_num=int(input("please enter the staring number"))
ending_num=int(input("please enter the ending number"))
prime_number(starting_num,ending_num)


num=int(input("please enter the number here"))


def print_factors(number):
    print(f"The factors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


num = int(input("Enter a number: "))

# Call the function to print factors
print_factors(num)

count=0  
num=1
while(count<20):
    print(num,end=" ")
    num=num+2
    count=count+1


year=int(input("please enter the year"))
         
if (year%100==0 and year%400==0):
         print("it is a leap year")
        
elif(year%100==0 and year%400!=0):
    print("it is not a leap year")
         
elif(year%4==0):
    print("it is a leap year")
    
else:
    print("it is not a leap year")
    
    

count=0
for i in range(2000,2101):
    if (i%100==0 and i%400==0):
        print(i)
    elif(i%100==0 and i%400!=0):
        continue
    elif(i%4==0):
        print(i)
    else:
        continue
            




def print_factors(number):
    count=0
    num=number
    print(f"The factors of {num} are:")
    for i in range(1, number + 1):
        if num % i == 0:
            count=count+1
    print(count)            
            
num = int(input("Enter a number: "))

# Call the function to print factors
print_factors(num)

#input a number and prints its prime or not. hint: a number is prime if it has only 2 factors
num=int(input("enter the number"))
factors=0
for i in range (1,num+1):
    if(num%i==0):
        factors=factors+1
if(factors==2):
    print("prime number")      
else:
    print("not a prime number")

count=0  
num=1
while(count<20):
    print(num,end=" ")
    num=num+2
    count=count+1


start = 1
count = 0
while(count!=20):
    print(count,"=",start)  
    start=start+2
    count=count+1

num=int(input("please enter the number"))
reversed_num=0
while(num!=0):
    digit= num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print(reversed_num)    


num=int(input("please enter the number"))
count=0
while(num!=0):
    last=num%10
    count=count+1
    num=num//10
print(count)

    
    

num=int(input("please enter the number"))
square=1
while(num!=0):
    last=num%10
    square=num*last
    num=num//10
print(square)    

#enter the number and print only odd numbers for eg:- 39484 print only 39

num=int(input("please enter the number"))
while(num!=0):
    last=num%10
    if(last%2!=0):
        print(last)
        num=num//10   

#enter the number and print only odd numbers for eg:- 39484 print only 39
num=int(input("please enter the number"))

while(num!=0):
    last=num%10
    if(num%2==0):
         num=num//10 
print(num)

#armstrong 146 1^3 + 4^3 + 6^3

num=146
while (num!=0):
    last=num%10
    m=last**3
    num=num//10
    
    print()
    



#armstrong 146 1^3 + 4^3 + 6^3
num=int(input("please enter the number"))

sum=0
temp=num
while (temp!=0):
    last=temp%10
    m=last**8
    sum=sum+m
    temp=temp//10
    print(sum)
if sum==num:
    print("it is an armstrong number")
else:
    print("its a not an armstrong number")
    
    

count=0
total=0

while count<=100:
    total=total+count
    count=count+1
    print(total, end =" ")
        
    
    


    

num=int(input("please enter the number"))
count=0
sum=0
while(num!=0):
    m=num%10
    if (m%2==0 and m!=0):
        sum=sum+m
        m=num//10
        print(sum)

num=input("please enter the phone number ")

if (len(num)==10 and num[0] in '6789'): 
    print("it is a valid number")
else:
    print("it is not invalid number")
    

num=int(input("please enter the number"))
count=0
while(num!=0):
        count=count+1
        num=num//10
print(count)

num=int(input("please enter the number"))
odd_count=0
even_count=0
while(num!=0):
    d=num%10
if d%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
num=num//10
print(even_count,odd_count)
    
    

year=int(input("please enter the year"))

if (year%100==0) and (year%400==0):
    print("i")
elif (year%4==0 and year%100!=0):
    print("i")
else:
    print("i")


start_year=int(input("please enter the year"))
end_year=int(input("please eneter the year"))

for i in range(start_year, end_year+1):
    if(i%100==0 and i%400==0):
        
        
import calendar

year=int(input("please enter the year"))
month=int(input("please enter the month"))

print(calendar.month(year,month))

import calendar
year=int(input("please enter the year"))


print(calendar.year(year))

import calendar 

date=int(input("please enter the date of the month"))
month=int(input("please enter the month of of the year"))
year=int(input("please enter the year"))

weekday=calendar.weekday(year,month,date)
print(weekday)

if weekday==0:
    print("monday"),
elif weekday==1:
    print("tuesday"),
elif weekday==2:
    print("wednesday"),
elif weekday==3:
    print("thursday"), 
elif weekday==4:
    print("friday"),
elif weekday==5:
    print("saturday"), 
elif weekday==6:
    print("sunday"),    


#Write a program to print all the months that have 30 days in 2024
calendar.monthrange(2024,9)


sum=0
for i in range(1,51,2):
    sum=sum+i
print(sum)
for i in range(2,51,2):
    sum=sum+i
print(sum)    

sum=0
for i in range(2,52,2):
    sum=sum+i
print(sum) 

a=2
b=3

x=a**5+b**3
y=a**7+b**4


sum=x+y
print(sum)

