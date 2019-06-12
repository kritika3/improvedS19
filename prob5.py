#!/usr/Python3

import datetime
name=input("Enter your name")
currentTime=datetime.datetime.now()
if currentTime.hour < 12:
    print('Good Morning'+" "+name)
if currentTime.hour > 12:
    print('Good Afternoon'+" "+name)
if currentTime.hour > 18:
    print('Good Evening'+" "+name)

