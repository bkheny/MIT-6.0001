# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:09:38 2022

@author: bobby
"""

low = int(0)
high = int(10000)
percent_saved = (low + high)/2.0

current_savings = 0
annual_salary = int(input("What is your starting anual salary? "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = total_cost * 0.25
epsilon = 100

r = 0.04

total_months = 0
steps = 0
while True:
    current_savings = 0
    monthly_salary = annual_salary/12
    for i in range(1,37):
        current_savings += (current_savings*r/12)
        current_savings += (monthly_salary * (percent_saved / 10000))     
        total_months += 1
        if total_months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    steps +=1   

    if abs(current_savings - portion_down_payment) <= epsilon:
        print("Steps in bisectional search: ", steps)
        best_savings_rate = percent_saved / 10000
        print("Best savings rate:", round(best_savings_rate,4))
        break
    elif (portion_down_payment - epsilon) - current_savings > 0:
        low = percent_saved
        percent_saved = (low + high) / 2.0
    else:
        high = percent_saved       
        percent_saved = (low + high) / 2.0

    if percent_saved >= 9999:
        print("It is not possible to afford this in 3 years")
        break