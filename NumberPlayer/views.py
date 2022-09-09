import numbers
from django.http import HttpResponse
from django.shortcuts import render

def isPalindrom(number):
    n = int(number)
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return temp==rev

def factorial(number):
    number = int(number)
    from math import factorial
    return factorial(number)

def isArmstrong(number):
    num = int(number)
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

def isEven(number):
    number = int(number)
    return number%2==0

def isOdd(number):
    number = int(number)
    return number%2!=0

def isAbundant(number):
    n = int(number)
    sum1=1 # 1 can divide any number 

    for i in range(2,n):
        if(n%i==0):    #if number is divisible by i add the number 
            sum1 = sum1+i

    return sum1>n

def binary(number):
    number = int(number)
    return bin(number)[2:]


def home(request):
    if request.method == "POST":
        
        number = request.POST.get('number')
        checkType = request.POST.get('dropdown')
        if not number.isnumeric():
            ans = "Please Enter Number only!!"
            desc = ""
        elif checkType == "Armstrong Number":
            ans = isArmstrong(number)
            desc = "Armstrong number is a number that is equal to the sum of cubes of its digits."
        elif checkType == "Palindrom Number":
            ans = isPalindrom(number)
            desc = "A palindromic number is a number (such as 16461) that remains the same when its digits are reversed."
        elif checkType == "Factorial":
            ans = factorial(number)
            desc = "A factorial is a function that multiplies a number by every number below it till 1."
        elif checkType == "Abundant Number":
            ans = isAbundant(number)
            desc = "An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number."
        elif checkType == "Binary Conversion":
            ans = binary(number)
            desc = "In decimal to binary conversion, we convert a base 10 number to a base 2 number "
        elif checkType == "Even Number":
            ans = isEven(number)
            desc = "A whole number that is able to be divided by two into two equal whole numbers"
        elif checkType == "Odd Number":
            ans = isOdd(number)
            desc = "Odd numbers are whole numbers that cannot be divided exactly into pairs."
        else:
            ans = ''
            desc = ""

        context ={
            'number':number,
            'type': checkType,
            'ans':ans,
            'desc': desc
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')
    