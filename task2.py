'''
##### Task 2 Compound Interest
Ask the user to enter the following:
* The principal (amount invested or borrowed)
* The annual interest rate (expressed as a percent)
* The number of compounding periods per year
* The length of time for the investment
Calculate the final amoutn as well as the amount of interest earned. Round your answer to 2 decimal places

```
https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
Enter the Princial: 2000
Enter the annual interest rate as a percent: 0.04
Enter the number of compounding periods: 4
How long is the investment period in years: 3
Your final amount is $2253.65
You earned $253.65 interest

Enter the Princial: 25000
Enter the annual interest rate as a percent: 0.075
Enter the number of compounding periods: 12
How long is the investment period in years: 6
Your final amount is $39152.94
You earned $14152.94 interest
```
'''
question = "What is the principal?"
p = input(question)
p = float(p)
question = "What is the annual interest day?"
r = input(question)
r = float(r)
question = "What is the number of compounding periods per year?"
n = input(question)
n = float(n)
question = "What is the length of time for the investment?"
t = input(question)
t = float(t)

a = p*(1+r/n)**(n*t)
a = round(a,2)
print(f"The final amount is ${a}.")
i = a - p
i = round(i,2)
print(f"The amount of interest earned is ${i}.")