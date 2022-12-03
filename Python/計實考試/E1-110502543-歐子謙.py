"""
Exam 1
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
while 1:
    n=input()
    if n == 'stop':
        break
    N=int(n)
    W=int(input())
    H=int(input())
    T=int(input())
    F=int(input())
    S=input()
    for j in range(F):
        for i in range(T):
            print(N*(W*S))
        for i in range(H-2*T):
            print(N*(T*S+(W-T*2)*' '+T*S))
        for i in range(T):
            print(N*(W*S))
