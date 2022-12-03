"""
Practice 6
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
test=open("test.txt","r")
list=test.readlines()
def F(n):
    x=0
    num=str(n)
    if n>0 and n%2==0:
        return 2+F(n//2)
    elif n>0 and n%2!=0:
        for j in range(len(str(n))):
            x+=int(num[j])
        return 3+F(x-5)
    else:
        return 0
for i in range(len(list)):
    num=list[i]
    n=int(num)
    print(F(n))

