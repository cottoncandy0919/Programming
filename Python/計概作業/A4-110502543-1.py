"""
Assignment 4
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
score=open("score.txt","r")
OUT=open("score_110502543.txt","w")
line=score.readlines()
print(line[0],file=OUT,end='')
for i in line[1:]:
    words =i.split()
    num = int(words[1])+int(words[2])+int(words[3])+int(words[4])
    sum=int(num)
    average= float(sum)/4
    print(i.strip('\n'),average,file=OUT)
score.close()




