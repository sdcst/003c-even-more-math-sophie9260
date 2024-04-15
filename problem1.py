#!python3

# Canada Income Tax Calculator part I

'''
It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
Python to determine Federal and Provincial Income Tax.

The Canadian income tax system is a tiered system, which means you pay different percentages of
your income for different parts of your income.
You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
20.5% on amounts over 49020 that are less than 98040
26% on amounts over 98040 but less than 151978
29% on amounts over 151978 but less than 216511
33% on amounts over 216511

Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

Example:
Enter your income: 125000
Your federal income tax is: 24411.7

'''

question = "what is the income?"
i = input(question)
i = float(i)
a = i - 49020

if i <= 49020: 
    a = 0.15*i 
    print(a)

elif 49020 < i < 98040:
    a= 49020*0.15
    b = i - 49020
    c = b*0.205
    print(c+a)

elif 98040 < i < 151978:
    a= 49020*0.15
    b= 49020*0.205
    c = i - 98040
    d = c*0.26
    abd = a+b+d
    abd = round(abd,2)
    print(abd)

elif 151978 < i < 216511:
    a= 49020*0.15
    b= 49020*0.205
    c = 53938*0.26
    d = i - 151978
    e = 0.29*d
    abce = a+b+c+e
    abce = round(abce,2)
    print(abce)

elif i >= 216511:
    a= 49020*0.15
    b= 49020*0.205
    c = 53938*0.26
    d = 64533*0.29
    e = i - 216511
    f = 0.33*e
    abcdf = a+b+c+d+f
    abcdf = round(abcdf,2)
    print(abcdf)
