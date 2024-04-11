#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  
Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""

import math 

question = "what is the lenght in centimeters?"
c = input(question)
c = float(c)
c = round(c)

f = c/30.48
ff = f%1

f = (math.floor(f))

i = ff*12
i = round(i)


print(f"{c} centimeters is {f} feet and {i} inches.")

