# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:19:50 2018

@author: Kiran H T
"""

import csv
def satisfy(d,h):
    for i in range(len(h)):
        if not (h[i]=='?' or h[i]==d[i]):
            return False
    return True

def specialise(d,g,x):
    g1=[]
    for h in g:
        if satisfy(d,h):
            for i in range(len(x)):
                if h[i]!='?':
                    continue
                s=x[i]
                for j in s:
                    if j==d[i]:
                        continue
                    h[i]=j
                    g1.append(h.copy())
                h[i]='?'
        else:
            g1.append(h)
    return g1

def generalise(d,s,x):
    for i in range(len(s)):
        if s[i]=='%':
            s[i]=d[i]
            x[i]=x[i].intersection({s[i]})
        elif s[i]!='?' and s[i]!=d[i]:
            s[i]='?'
            x[i]=set()
    return s

with open('Training_examples.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    data=[]
    for row in csv_reader:
        data.append(row)
        
s=['%']*(len(data[0])-1)
g=[]
g.append(['?']*(len(data[0])-1))
f=True
x=[]
for i in range(len(data[0])-1):
    x.append(set())
for d in data:
    for i in range(len(d)-1):
        x[i].add(d[i])

print("S:  ",s,"\nG:  ",g,"\n")
for d in data:
    print("Data:",d)
    if d[-1]=="yes":
        s=generalise(d,s,x)
        g1=[]
        for h in g:
            if satisfy(d,h):
                g1.append(h)
        g=g1
    else:
        if satisfy(d,s):
            f=False
            break
        g=specialise(d,g,x)
        
    print("S:  ",s,"\nG:  ",g,"\n")
if f==False:
    print("Hypothesis set cant be formed.")
else:
    print("S:  ",s,"\nG:  ",g,"\n")