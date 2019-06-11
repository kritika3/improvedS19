#!/usr/Python3

import webbrowser
from googlesearch import search
print('Enter URL')
query=input()
for i in search(query,stop=10):
    print(i)
