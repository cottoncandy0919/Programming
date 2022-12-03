"""
Exam 3
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
while 1:
    str=input()
    if str == '-1':
        break
    min=0
    for ele in str:
        if min<ord(ele):
            min=ord(ele)
    if min <= 57:
        min-=48
    elif min<=90:
        min-=55
    elif min <=122:
        min-=61
    min+=1
    base=0
    for n in range(min,63):
        power = str.__len__() -1
        digit = 0
        for ele in str:
            k=ord(ele)
            if k>=48 and k <= 57:
                k-=48
                digit += n**power*k
                power-=1
            elif k>=65 and k<=90:
                k-=55
                digit+=(n**power)*k
                power -=1
            elif k>=97 and k<=122:
                k-=61
                digit +=(n**power)*k
                power-=1
        #print(digit)
        answer=digit%(n-1)
        if answer ==0:
            base = n
            print(base)
            break
    if base==0:
        print("such number is impossible!")
