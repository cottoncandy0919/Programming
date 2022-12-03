"""
Practice 2
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
import random
flag=random.randint(1,100)
N = 1
while 1:
    input1 = int(input("輸入一數字 : "))
    if input1 < flag:
        print("比", input1,"還要大")
        N += 1
    elif input1 > flag:
        print("比", input1,"還要小")
        N += 1
    else:
        print("猜對了！總共猜了 ",N ," 次")
        break