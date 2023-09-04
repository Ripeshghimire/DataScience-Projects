import numpy as np 
import pandas as pd 
df = pd.read_csv('fifa21/fifa21_raw_data.csv')
print(df.columns)
height = df['Height']
weight = df['Weight']
print(height.head())
print(weight.head())
# • Do the height and weight columns have the appropriate data types?
print(height.dtype)
print(weight.dtype)
def makeNumericheight(item):
    if '"' in item:
        return item[:item.find('"')]
height2 = height.apply(makeNumericheight)
# print(height2)
def height(item):
    feet, inches = map(int, item.split("'"))
    item = feet * 12 + inches
    return item
height3 = height2.apply(height)
# print(height3.dtype)
df['Height'] = height3
# print(df['Height'])
def makeNumericWeight(item):
    if 'l' in item:
        item  = item[:item.find('l')]
        return int(item)
weight2 = weight.apply(makeNumericWeight)
print(weight2)
df['Weight'] = weight2
# print(df['Weight'])


# • Can you separate the joined column into year, month and day columns?
print(df.columns)
dob = df['Joined']
def getYear(item):
    if ', ' in item:
        item = item[item.find(', ')+1:]
        return(int(item))
year = dob.apply(getYear)
# print(year)
df['year'] = year
def getMonth(item):
    if ',' in item:
        item = item[:item.find(' ')]
        return item
month = dob.apply(getMonth)
# print(month)
df['Month'] = month
def getDays(item):
    if ',' in item:
        item = item[item.find(' '):item.find(',')]
        return int(item)
days = dob.apply(getDays)
df['Days'] = days
# print(df['Days'])
# Can you clean and transform the value, wage and release clause columns into columns of integers?
value = df['Value']
# print(value.sample(10))
def numericValue(item):
    if '€' in item:
        item = item[item.find('€')+1:]
    if 'K' in item:
        item = item[:item.find('K')]
        item_numeric = float(item) * 1000
        return item_numeric
    if 'M' in item:
         item = item[:item.find('M')]
         item = float(item) * 1000000
    return float(item)
valueMoney = value.apply(numericValue)
df['Value'] = valueMoney
# print(df['Value'])
# • How can you remove the newline characters from the Hits column?
hits = df['Hits']
def removenewLine(item1):
    if '\n' in str(item1):
        item1 = item1.replace('\n','')
        return item1
hits2 = hits.apply(removenewLine)
hits = hits2
print(hits)
# • Should you separate the Team & Contract column into separate team and contract columns?
teamandcontract = df['Team & Contract']
print(teamandcontract.sample(5))
