# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:09:38 2022

@author: bobby
"""
#inputs
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#initialize variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04

monthly_salary = annual_salary/12

months = 0
downpayment = portion_down_payment*total_cost

#code
while current_savings < downpayment:
    current_savings += current_savings * r/12
    current_savings += portion_saved*monthly_salary
    if months%6 == 0 and months !=0:
        monthly_salary = monthly_salary*(1+semi_annual_raise)
    months += 1
    
#print results
print("Number of months:", months)