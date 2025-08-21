def add(num1,num2):
    add=num1+num2
    print("addition is ",add)
def multiply(num1,num2):    
    multiply=num1*num2
    print("multiplication is ", multiply)
def divide(num1,num2):    
    divide=num1/num2
    print("divison is",divide)
def sub(num1,num2):    
    sub=num1-num2
    print("substraction is ",sub)
    
add(5,9)
multiply(9,8)
divide(9,2)
sub(8,6)
    

num1=int(input("enter the number 1"))
num2=int(input("enter the number 2"))
operator=input("enter the opearation you want to do")

if operator=="*": 
    print(num1*num2),
elif operator=="/":
    print(num1/num2),
elif operator=="+": 
    print(num1+num2),
elif operator=="-":
    print(num1-num2),

#Question 1- Create a function that takes 3 numbers as the input and prints the largest amongst them.

def largeNumber(num1,num2,num3):
    if (num1>num2) and (num1>num3):
        print("largest number is",num1)
   
    elif(num2>num1) and (num2>num3):
        print("largest number is ",num2)
    
    elif(num3>num1) and (num3>num2):
        print(num3)
    
    else:
        print("invalid number")
    
num1=int(input("please enter the number"))
num2=int(input("please enter the number"))
num3=int(input("please enter the number"))
largeNumber(num1,num2,num3)

def triangleType(side1,side2,side3):


    if side1+side2==side3:
        print("right triangle"),
    elif side1==side2==side3:
        print("equilateral triangle"),
    elif side1==side2 or side1==side3 or side2==side3:
        print("isosceles triangle")
    else:
        print("scalene triangle")
    
side1=int(input("enter the length of side 1 "))
side2=int(input("enter the length of side 2 "))
side3=int(input("enter the length of side 3 "))
    

triangleType(side1,side2,side3)

#Question 4 - Create a function that takes a number as input from the user and prints the
#maximum 4 digit number that it completely divides.
maxim=0
def maxi(num):
    for i in range(1000,9999,1):
        if i%num==0:
            maxim=i
print(max)
               
            
num=(int(input("please enter the number")))            
max(num)       

##Question 4 - Create a function that takes a number as input from the user and prints the
# minmum 3 digit number that it completely divides.

def min(num):
    for i in range(100,999,1):
        if i%num==0:
            print(i)
            break
        
            
num=int(input("please enter the number")) 
min(num)

#Simple Interest:
#Write a program to calculate the simple interest using the formula: SI = (P x R x T) / 100
def simple_int(p,r,t):
    si=(p*r*t)/100
    return si

result=simple_int(1000,5,2)
print(result)



#Write a Python Function that takes a number as the input and returns the 
#reverse of that number.

num=int(input("enter the number"))
def reverse_num():
    while(num!=0):
        m=num%10
        print(m)
        num=num//10
    return reverse_num

result=reverse_num()
print(result)


def area_of_rectangle(l,b):
    return l*b

area=area_of_rectangle(20,10)
print(area)

def hours_mins(mins):
    return 


mins=int(input("please enter the minutes "))

num=int(input("please enter a number"))
square= lambda num: num**2 
print(square(5))

num=int(input("please enter a number"))
cube= lambda num: num**3 
print(cube(num))

temp_in_celcius=int(input("please enter the temperature in celcius"))
fahrenheit= lambda temp_in_celcius:(temp_in_celcius * 1.8) + 32 
print(fahrenheit(temp_in_celcius))

#[TRICKY] Question 5:
#Write a lambda function that takes a number and returns the largest of them.
largest_num=lambda x,y: x if x > y else y
print(largest_num(6,8))

#Write a lambda function that takes 3 numbers
#as input and returns the number that is divisible by 3.
num1=int(input("please enter the number ="))
num2=int(input("please enter the number ="))
num3=int(input("please enter the number ="))

divisible_by_3 = lambda num1,num2,num3: num1 if (num1%3==0)  else(num2) if(num2%3==0) else(num3)   

print("the number divisible by 3 is",divisible_by_3(num1,num2,num3))

#: Write a lambda function that calculates the factorial of a number
num=int(input("please enter the number"))
factorial=lambda num : factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(factorial(num))


#Write a lambda function that takes 2 numbers as input and returns the LCM of the two numbers.

num1=int(input("please enter a number"))
num2=int(input("please enter a number"))
num3=int(input("please eneter a number"))

largest= lambda num1,num2,num3 : num1 if (num1>num2) and (num1>num3) else num2 if (num2>num1) and (num2>num3) else num3 
 
print(largest(num1,num2,num3))

#Write a lambda function that takes 2 numbers as input and returns the HCF of the two numbers
import math

num1=int(input("please enter a number"))
num2=int(input("please enter a number"))

HCF= lambda num1,num2: math.gcd(num1,num2)

print(HCF(num1,num2))

import math

num1=int(input("please enter a number"))
num2=int(input("please enter a number"))

HCF= lambda num1,num2: math.gcd(num1,num2)
LCM=num1*num2//(HCF(num1,num2))

print(HCF(num1,num2))
print(LCM)

num=int(input("please enter a number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial)

import math

num1=int(input("please enter a number"))
num2=int(input("please enter a number"))

HCF= lambda num1,num2: math.gcd(num1,num2)
LCM=num1*num2//(HCF(num1,num2))

print(HCF(num1,num2))
print(LCM)

num1=int(input("please enter a number"))
num2=int(input("please enter a number"))
num3=int(input("please enter a number"))

def greatest_num(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("num1 is the greatest number")
    elif(num2>num1 and num2>num3):
        print("num2 is greatest number")
        
    else:
        print("num3 is the greatest number")
        
result=greatest_num(num1,num2,num3)
print(result)

#how to print the time taken to exceute the whole program

#how to print the absoulte value of the number

num=int(input("please input a number"))

print(abs(num))

#write a function that uses lambda to multiply two numbers
num1=int(input("please enter a number"))
num2=int(input("please enter a number"))

multiply= lambda num1,num2: num1*num2
answer=multiply(num1,num2)
print(answer)

#write a lambda function which takes cube of a number

num1=int(input("please enter a number"))
cube=3

cube_of_the_number=lambda num1,cube: num1**3

answer=cube_of_the_number(num1,cube)
print(answer)

#write a function is_prime() if the argument pass to it is a
#prime and 0 otherwise
def prime_number(num):
    factors=0
    for i in range (1,num+1):
        if(num%i==0):
            factors=factors+1
    if(factors==2):
        print("prime number")      
    else:
        print("not a prime number")
num=int(input("enter the number"))
prime_number(num)


#write a function which accepts integer between 1 and 12 to 
#represent the months of the year.
num=int(input("please enter the a number to see which month it represnts"))
def number_to_months():
    if(num==1):
        print("january")
    elif(num==2):
        print("feburary")
    elif(num==3):
        print("March")
    elif(num==4):
        print("April")
    elif(num==5):
        print("May")
    elif(num==6):
        print("June")
    elif(num==7):
        print("July")
    elif(num==8):
        print("August") 
    elif(num==9):
        print("September")
    elif(num==10):
        print("October")
    elif(num==11):
        print("November")
    elif(num==12):
        print("December")
    else:
        print("invalid number")
    
answer=number_to_months()
print(answer)

#check whether the function is a leap year 
import calendar
year=int(input("please enter the year"))

is_leap=(calendar.isleap(year))
if (is_leap==True):
    print("this is a leap year",year)
else:
    print("this is not a leap year")
    


#create a program which converts fibonacci series without recurrsion

def f_series(n):
    first=0
    second=1
    
    for i in range(3,n):
        sum=first+second
        print(sum,end=' ')
        first=second
        second=sum
            
f_series(10)

#sort the numbers
def sort(a,b,c):
    if a>b>c:
        return True
    elif a<b<c:
        return True
    else:
        return False
    
sort(9,100,6)    

number=input("please enter a valid phone number")
first=number[0]
digits=len(number)
if(first in ('6','7','8','9') and digits==10):
    print("valid number")
else:
    print("invalid")

    


#write a program to find the number is authmorphic a number is considered authmorphic if the numbers is 25*2 is 625 beacause 
# 25 is present in the number 625

num=input("please eneter a number")
length=len(num)
int_num=int(num)
sq=int_num**2
str_sq=str(sq)
last_digits=str_sq[-length:]
if(int(last_digits)==int_num):
    print("automorphic")
else:
    print("not a automorphic")

    
    

#write  a program if the number is neon number or not

num=1
sq=num**2
summ_of_squares=0

while(sq!=0):
    ld=sq%10
    summ_of_squares=summ_of_squares+ld
    sq=sq//10
if (summ_of_squares==num):
    print("it is a Neon number")
    
else:
    print("not a neon")
    

num=6
sq=36

#we assume the number is one digit
ld=sq%10
if(ld==num):
    print("automorphic")
else:
    print("automorphic")

# a buzz number is a number which is either divisible by 7 or which ends with 7

num=14
buzz_num=0

if(num%10==7 or num%7==0):
    print("the number is a buzz number")
else:
    print("the number is not a buzz number")

# a niven number is a number which is sum of the numbers and the result is also divisible by same number
#eg:- 126=1+2+6=9 and 126/9
num=125
sum_sq=0

while(num!=0):
    ld=num%10
    sum_sq=sum_sq+ld
    num=num//10

if(num%sum_sq==0 and sum_sq==num):
    print("it is a niven number")
else:
    print("it is not a niven number")
print(sum_sq)    #doubt

#SPY number is a number is a number where sum of the digit and the product of the digits is the same
#eg:-num=1124 ,1+1+2+4=8,1*1*2*4=8

num=118
sum_d=0
pro_d=1

while(num!=0):
    ld=num%10
    sum_d=sum_d+ld
    pro_d=pro_d*ld
    num=num//10
if(sum_d==pro_d):
    print("the number is a spy number")
else:
    print("the number is not a spy number")
print(pro_d)
print(sum_d)   ##doubt 

#write a program to write numbers between 150 to 250 and divisible by 5

for i in range(150,251):
    if (i%5==0):
        print(i)


#write a program where you calculate the base and power using two inputs from the user

base=int(input("please enter the base number"))
power=int(input("please enter the power of the number"))


num=(base)**power
print(num)

#write a program to classify between prime and composite
# a prime number has 2 factors: 1 and the number it self and composite has more than two factors

num=int(input("enter the number"))
factors=0
for i in range (1,num+1):
    if(num%i==0):
        factors=factors+1
if(factors==2):
    print("prime number")      
elif(factors>2):
    print("composite number")
else:
    print("invalid number")




#write a program to reverse a number
num=4590

while(num!=0):
    ld=num%10
    print(ld,end='')
    num=num//10
     
    
    

#write a program that asks user for number until user enters zero

num=int(input("please enter a number"))
summ=0
while(num!=0):
    ld=num%10
    summ=summ+ld
    num=num//10
print(summ)    
    


num=1
while(num<=10):
    print("5","*",num,"=",num*5)
    num=num+1
    

#write a program to see how many even numbers are there in the number

num=545186
count=0
while(num!=0):
    ld=num%10
    if(ld%2==0):
        count=count+1
        print(ld,end=' ')
    num=num//10
print("count=",count,end='')    

