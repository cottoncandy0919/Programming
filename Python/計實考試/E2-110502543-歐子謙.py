"""
Exam 2
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
text1=open('invoice.txt','r')
text2=open('num.txt','r')
invoive=text1.readlines()
num=text2.readlines()
arr1=[]
arr2=[]
a,b,c,d,e,f,g,h=0,0,0,0,0,0,0,0
for i in num:
    win=i.split()
    arr1.append(win)
for j in invoive:
    arr2.append(j.split())
for i in range(len(arr2)):
    if arr1[0][0]== arr2[i][0]:
        a+=1
    elif arr1[1][0]==arr2[i][0]:
        b+=1
    elif arr1[2][0]==arr2[i][0]:
        c+=1
    elif arr1[3][0]==arr2[i][0]:
        c+=1
    elif arr1[4][0]==arr2[i][0]:
        c+=1
    elif arr1[2][0][1:]==arr2[i][0][1:]:
        d+=1
    elif arr1[3][0][1:]==arr2[i][0][1:]:
        d+=1
    elif arr1[4][0][1:]==arr2[i][0][1:]:
        d+=1
    elif arr1[2][0][2:]==arr2[i][0][2:]:
        e+=1
    elif arr1[3][0][2:]==arr2[i][0][2:]:
        e+=1
    elif arr1[4][0][2:]==arr2[i][0][2:]:
        e+=1
    elif arr1[2][0][3:]==arr2[i][0][3:]:
        f+=1
    elif arr1[3][0][3:]==arr2[i][0][3:]:
        f+=1
    elif arr1[4][0][3:]==arr2[i][0][3:]:
        f+=1
    elif arr1[2][0][4:]==arr2[i][0][4:]:
        g+=1
    elif arr1[3][0][4:]==arr2[i][0][4:]:
        g+=1
    elif arr1[4][0][4:]==arr2[i][0][4:]:
        g+=1
    elif arr1[2][0][5:]==arr2[i][0][5:]:
        h+=1
    elif arr1[3][0][5:]==arr2[i][0][5:]:
        h+=1
    elif arr1[4][0][5:]==arr2[i][0][5:]:
        h+=1
    elif arr1[5][0]==arr2[i][0][5:]:
        h+=1
    elif arr1[6][0]==arr2[i][0][5:]:
        h+=1
    elif arr1[7][0]==arr2[i][0][5:]:
        h+=1
print('特別獎 :',a)
print('特獎 :',b)
print('頭獎 :',c)
print('二獎 :',d)
print('三獎 :',e)
print('四獎 :',f)
print('五獎 :',g)
print('六獎 :',h)
print('沒中獎 :',len(arr2)-a-b-c-d-e-f-g-h)
sum=10000000*a+2000000*b+200000*c+40000*d+10000*e+4000*f+1000*g+200*h
print(sum)