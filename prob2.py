#!/usr/Pyhton3

from sys import argv
argv=input()
print(argv)
import datetime
from datetime import date
today=str(datetime.date.today)
curr_year=int(today[:4])
print('Enter name')
name=input()
print('Enter your age')
curr_age=int(input())
age=95-curr_age
print('Year in which you will be 95 is : ')
y=curr_year+age
print(y)

