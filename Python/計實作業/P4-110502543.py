"""
Practice 4
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
test=open("test.txt","r")
OUT=open("ans-110502543.txt","w")
line = test.readlines()
for j in line:
    words = j.split('=')
    for i in range(0,len(words),2):
        if eval(words[i]) == int(words[i+1]):
            print('T',file=OUT)
        else:
            print('F',file=OUT)
test.close()
