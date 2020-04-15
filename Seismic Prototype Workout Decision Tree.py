import numpy as np
import pandas as pd
from sklearn import tree

input_file = "Seismic Spine Check Chart Train Data TEST 1.csv"

input_file2 = "Seismic Hip Hing Test TEST 1.csv"

df = pd.read_csv(input_file, header=0)

df2 = pd.read_csv(input_file2, header=0)

df
df2

y = df["Exercises"]

y2 = df2["Exercises"]

X = df[["Kyphosis", "Lordosis", "Scoliosis"]]

X2 = df2[["Round Back", "Squatting Confusion", "Knees Locked", "Full Range of Motion"]]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

clf2 = tree.DecisionTreeClassifier()
clf2 = clf2.fit(X2,y2)

# produces exercise list decisions for ranges 0-10 of spine conditions

d = clf.predict([[0, 1, 0]])

print (d)

list = []


def new_print(d):
    if d == '1,2':
        list.append('Exercise 1')
        list.append('Exericse 2')
        list.append('Exericse 0')
    if d == '2,6':
        list.append('Exercise 2')
        list.append('Exercise 5')
        list.append('Exericse 8')
    if d == '3,4':
        list.append('Exercise 4')
        list.append('Exercise 3')
        list.append('Exercise 7')
    
new_print(d)
print(list)

while list.count('Exercise 3') > 1:
    list.remove('Exercise 3')
    if list.count('Exercise 3') == 1:
        break

while list.count('Exercise 4') > 1:
    list.remove('Exercise 4')
    if list.count('Exercise 4') == 1:
        break
        
while list.count('Exercise 5') > 1:
    list.remove('Exercise 5')
    if list.count('Exercise 5') == 1:
        break
        
while list.count('Exercise 6') > 1:
    list.remove('Exercise 6')
    if list.count('Exercise 6') == 1:
        break
        
while list.count('Exercise 2') > 1:
    list.remove('Exercise 2')
    if list.count('Exercise 2') == 1:
        break

while list.count('Exercise 1') > 1:
    list.remove('Exercise 1')
    if list.count('Exercise 1') == 1:
        break
        
while list.count('Exercise 7') > 1:
    list.remove('Exercise 7')
    if list.count('Exercise 7') == 1:
        break

while list.count('Exercise 0') > 1:
    list.remove('Exercise 0')
    if list.count('Exercise 0') == 1:
        break
while list.count('Exercise 8') > 1:
    list.remove('Exercise 8')
    if list.count('Exercise 8') == 1:
        break
        
print(list)

# ran an experiment to create a list of exercises from a decision-
# -tree decision where based off the ranges of the spine malproperty-
# - the AI chooses a pair of number representing exercises
# then i made an if function adds exercises to list based off the combo nums
# then i made a while loop that filters out duplicate data from the list 

d2 = clf2.predict([[1,0, 1, 3]])

print (d2)


list2 = []

def new_print2(d2):
    if d2 == '1,2':
        list2.append('Exercise 1')
        list2.append('Exericse 2')
    if d2 == '2,5':
        list2.append('Exercise 2')
        list2.append('Exercise 5')
    if d2 == '3,4':
        list2.append('Exercise 4')
        list2.append('Exercise 3')
        list2.append('Exercise 7')
        
new_print2(d2)
print(list2)

while list2.count('Exercise 3') > 1:
    list2.remove('Exercise 3')
    if list2.count('Exercise 3') == 1:
        break

while list2.count('Exercise 4') > 1:
    list2.remove('Exercise 4')
    if list2.count('Exercise 4') == 1:
        break
        
while list2.count('Exercise 5') > 1:
    list2.remove('Exercise 5')
    if list2.count('Exercise 5') == 1:
        break
        
while list2.count('Exercise 6') > 1:
    list2.remove('Exercise 6')
    if list2.count('Exercise 6') == 1:
        break
        
while list2.count('Exercise 2') > 1:
    list2.remove('Exercise 2')
    if list2.count('Exercise 2') == 1:
        break

while list2.count('Exercise 1') > 1:
    list2.remove('Exercise 1')
    if list2.count('Exercise 1') == 1:
        break
        
while list2.count('Exercise 7') > 1:
    list2.remove('Exercise 7')
    if list2.count('Exercise 7') == 1:
        break
        
print(list2)

list3 = list2 + list 
print(list3)

if "Exercise 1" and "Exercise 8" in list3:
    list3.remove("Exercise 8")

if "Exercise 4" and "Exercise 5" in list3:
    list3.remove("Exercise 5")
    
print(list3)