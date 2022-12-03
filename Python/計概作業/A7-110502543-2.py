"""
Assignment 7
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
ANS = open('110502543.txt', 'w')
NUM = open('num.txt', 'r')
arr = []
for i in range(9) :
    arr.append(set())
arr[1].add("()")
for i in range(2, 4) :
    for j in arr[i-1] :
        arr[i].add("("+j+")")
        arr[i].add("()"+j)
        arr[i].add(j+"()")
for i in range(4, 9) :
    for j in arr[i-1] :
        arr[i].add("("+j+")")
        arr[i].add("()"+j)
        arr[i].add(j+"()")
    for j in range(2, i+1//2) :
        for k in arr[j] :
            for l in arr[i-j] :
                arr[i].add(k+l)
                arr[i].add(l+k)
n = int(NUM.readline())
if (n== 0) :
    print("none",end='', file=ANS)
    print("none",end='')
else :
    print(' '.join(arr[n]),end = '', file=ANS)
    print(' '.join(arr[n]),end = '')
print('\n110502543歐子謙',end='',file=ANS)
print('\n110502543歐子謙',end='')
ANS.close()
NUM.close()