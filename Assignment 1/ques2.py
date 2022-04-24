Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:25:35) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> tax_rate=0.20
>>> gross_income= int(input("enter your income"))
enter your income 100000
>>> standar_deduction = 10000
>>> dependents= int(input("enter number of dependents:"))
enter number of dependents:2
>>> dependent_deduction= 3000
>>> taxable_income =gross_income - standar_deduction - (dependents*dependent_deduction)
>>> tax= taxable_income*tax_rate
>>> print(tax)
16800.0
>>> 