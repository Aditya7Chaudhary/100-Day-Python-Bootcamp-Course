import random 
import math

letters = ['a','b','c','d','e','f']
numbers = ['1','2','3','4','5','6']
char = ['@','#','$','%']

l = int(input("Enter the number of letters you want"))
n = int(input("Enter the number of numbers you want"))
c = int(input("Enter the number of special characters you want"))

p = []
for i in range(l):
    p.append(random.choice(letters))
for i in range(n):
    p.append(random.choice(numbers))
for i in range(c):
    p.append(random.choice(char))

password = ""
r = len(p)
for i in range(r):
    random_char = random.choice(p)
    password += random_char
    p.remove(random_char)

print(f"The password generated is {password}")
