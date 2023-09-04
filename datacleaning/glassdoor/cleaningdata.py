import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Uncleaned_DS_jobs.csv')
# print(df.head(1).to_string())
company = df['Company Name']
# print(company.head())
# removing the the numbers that were in the company name
def companyName(item):
        return item[:item.find('\n')]
name = company.apply(companyName)
company = name
# print(company)

# make the salary columns into integer
salary = df['Salary Estimate']
print(salary)
def makeIntSalary(item):
        item = item[:item.find('(')]
        if '$' in item:
         item = item.replace(r'$','')
         item = item.replace(r'K', '')
        return (item)
sa = salary.apply(makeIntSalary)
print(sa)

# make a new state columns from the data
location = df['Location']
print(location.head())
def getState(item):
    item = item[item.find(',')+1:]
    return   item
state = location.apply(getState)
print(state.head(10))
df['State'] = state
print(df['State'])