# 1 SUM OF FIRST N POSITIVE INTEGERS

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "positive integers is:", total)


# 2Python program to count occurrences of a substring in a string 

string=input("enter string")
subs=input("enter subs")
count = string.count(subs)

print("Number of occurrences:", count)

# 3 to count ocurrence of each word in sentance

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in set(words):
    print(word, ":", words.count(word))



# 4 Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

new_str1 =   str2[:2]  + str1[2:] 
new_str2 =    str1[:2] + str2[2:] 

result = new_str1 + " " + new_str2

print("Result:", result)


# 7 Program to find Greatest Common Divisor of two numbers. For example, the
#GCDof20 and 28 is 4 and the GCD of 98 and 56 is 14


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

small = min(num1, num2)

for i in range(small, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print("GCD is:", i)
        break
# 15 Given a number n, write a Python program to make and print 
# the list of Fibonacci series up to n.


n = int(input("Enter number of terms: "))

# First two numbers
a = 0
b = 1

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 5Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged# Program to add 'ing' or 'ly' to a given string

string = input("Enter a string: ")

if len(string) < 3:
    print(string)
elif string.endswith("ing"):
    print(string + "ly")
else:
    print(string + "ing")


# 20 password generator

class User:
    def __init__(self, uid, name, password):
        self.data = (uid, name, password)   # storing in tuple

    def show(self):
        print("User Details:", self.data)


try:
    uid = int(input("Enter ID: "))
    name = input("Enter Name: ")
    word = input("Enter word: ")

    password = word + "123@"

    if len(password) < 8:
        password += "A"

    u = User(uid, name, password)

    print("Password:", password)
    u.show()

except:
    print("Invalid input")

# 19 series
import math
startno=int(input("enter the number"))
even0dd=input("even or odd")
noofit=int(input("enter the range"))
j=2
ans1=0
if even0dd=="even":
    j=2
else:
    j=1

for i in range(0,noofit):
    print(startno,"-",j,"-",math.factorial(j))
    ans=startno/math.factorial(j)
    print(ans)
    ans1+=ans
    j+=2
    startno+=2
print(ans1)
    
