"""
Assignment 6
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
#def F(num):
    #if num>=10:
    #return 1+F(num-22)+F(F(num-30)-30)
    #elif 9>=num or num>=5:
    #return 2+F(num-2)
    #else:
    #return 3
def F(n):
    if int(n) >= 10:
        return 1+F(int(n)-22)+F(F(int(n)-30)-30)
    elif int(n)<=9 and int(n)>=5:
        return 2+F(int(n)-2)
    else:
        return 3
while 1:
    n= input("number:")
    if n =='0':
        break
    else:
        if len(n)==n.count('0'):
            print('Error Message')
        else:
            a = 0
            for i in range(len(n)):
                if n[i] == '0' or n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '4' or n[i] == '5' or n[
                    i] == '6' or n[i] == '7' or n[i] == '8' or n[i] == '9':
                    a += 1
                else:
                    a += 0
            if len(n) == a and int(n) <=500:
                #print('n是個正整數且小於等於500')
                num=int(n)
                print(F(n))
            else:
                print('Error Message')

