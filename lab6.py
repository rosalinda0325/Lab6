
"""
This program will generate a random integer between 1 and 20 and based no
the result of the random number, we check to see if it falls under certain range
If the number is greater than 15, then it will print "cherries" 
otherwise if the number is greater > 10 then it will print "orange"
otherwise if the number is greater > 5 then it will print "plus"
otherwise if the number is greater > 2 then it will print "melon"
otherwise if the number is greater > 1 then it will print "bell"
if the number is not any of the above then it will print "bar"

we start by using a loop 3 times and print the results to the user. Example "plus cherries"

"""

"""
num = generate random number

if num is greater than 15
then it will print "cherries" 

otherwise if the num is greater > 10
then it will print "orange"

otherwise if the num is greater > 5 
then it will print "plus"

otherwise if the num is greater > 2 
then it will print "melon"

otherwise if the num is greater > 1 
then it will print "bell"

otherwise
the result will be "bar"

loop tree times
print the output (fruit) to the user

"""

import random

def main():
    for i in range(0, 3):
     spin()

def spin():
    rand_num = random.randint(1, 20)
output = ""
if(rand_num > 15):
    output = "Cherries"
elif(rand_num > 10):
    output = "Orange"
elif(rand_num > 5):
    output = "Plum"
elif(rand_num > 2):
    output = "Bell"
elif(rand_num > 1):
    output = "Melon"
else:
    output = "Bar"

print(output, end =" ")

main()