"""
Assignment 4
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
score=open("scoretest.txt","r")
list=score.readlines()
arr=[]
for i in list:
    arr.append(i.split())
subject=input("查詢項目: ")
name=input("姓名: ")
for i in range(1,6):
    if str.lower(arr[0][i]) == str.lower(subject):
        a=i
    else:
        continue
    for j in range(1,6):
        if str.lower(arr [j][0]) == str.lower(name):
            b=j
        else:
            continue
    print(arr[b][0],arr[0][a],arr[b][a])