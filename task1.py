'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
question = "What is the expected number?"
e = input(question)
e = float(e)
question = "What is the actual number?"
a = input(question)
a = float(a)

D = e - a

DP = D/e*100
DP = round(DP,2)

print(f"the percent difference is a decrease of {DP}%.")

question = "What is the expected number?"
e = input(question)
e = float(e)
question = "What is the actual number?"
a = input(question)
a = float(a)

I = a - e

IP = I/e*100.
IP = round(IP, 2)

print(f"the percent difference is an increase of {IP}%.")

