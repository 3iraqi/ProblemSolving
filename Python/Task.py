'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'col2': [444, 555, 666, 444, 333, 222, 666, 777, 666, 555],
                   'col3': ['abc', 'def', 'ghi', 'xyz', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']})

print(df)

print("\nGet number of rows")
print(len(df))

print("\nGet random 50% rows")
print(df.sample(frac=0.5))

print("\nSort by col1 , DESC")
print(df.sort_values(by='col1', ascending=False))

print("\nFilter data to get obtain result (col2 >=7 )")
print(df[df['col2'] >= 7])

print("\nGet the oldest 3 rows")
print(df.sort_values(by='col1', ascending=True).head(3)) 
'''

'''
name = input("Enter your name: ")
weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in CM: "))

bmi = weight / (height * height)

if bmi <= 18.5:
    print("Your BMI value is", bmi, "and you are: UNDERWEIGHT")
elif bmi > 18.5 and bmi <= 24.9:
    print("Your BMI value is", bmi, "and you are: NORMAL WEIGHT")
elif bmi > 24.9 and bmi <= 29.9:
    print("Your BMI value is", bmi, "and you are: OVERWEIGHT")
else:
    print("Your BMI value is", bmi, "and you are: OBESE") 
'''

'''
name = input("Enter your name: ")
department = input("Enter your department: ")

def grade(degree):
    if degree >= 90:
        return "Excellent"
    elif degree >= 80:
        return "Very_Good"
    elif degree >= 70:
        return "Good"
    elif degree >= 60:
        return "Pass"
    else:
        return "Fail"
degree = grade(int(input("Enter your degree: ")))

print("Hello " + name + ", your department is " + department + " and your grade is "+ degree)

'''