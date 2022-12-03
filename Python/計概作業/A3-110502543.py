"""
Assignment 3
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
test = open("test.txt","r")
line = test.readline()
words = line.split()
test.close()
answer = open("answer.txt","w")

def find_factor(a):
    b=[]
    for i in range(1,a+1):
        if a % i != 0:
            continue
        else:
            b.append(i)
    return b


def find_prime(b):
    if b == 1:
        return "N"
    for j in range(2,b):
        if b % j == 0:
            return "N"
            break
    return "Y"
for k in range(len(words)):
    print("Number_",k+1,":", " ", words[k],file=answer,sep="")
    for i in range(len(find_factor(int(words[k])))):
        print(find_factor(int(words[k]))[i],find_prime(find_factor(int(words[k]))[i]),file=answer)
    print('',file=answer)
answer.close()