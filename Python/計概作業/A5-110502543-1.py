"""
Assignment 5
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
def fun_1():
    while 1:
        BIN=input('Binary: ')
        DEC=0
        if BIN != "-1":
            for i in range(len(BIN)):
                DEC += int(BIN[len(BIN) - 1 - i]) * 2 ** (i)
            ANS = ""
            RUN=str(BIN).count("0")+str(BIN).count("1")
            if RUN == len(BIN):
                while DEC >0:
                    if DEC%16<10:
                        ANS+=str(DEC % 16)
                        DEC=DEC//16
                    elif DEC % 16 == 10:
                        ANS+="A"
                        DEC = DEC // 16
                        continue
                    elif DEC % 16 == 11:
                        ANS += "B"
                        DEC = DEC // 16
                        continue
                    elif DEC % 16 == 12:
                        ANS += "C"
                        DEC = DEC // 16
                        continue
                    elif DEC % 16 == 13:
                        ANS += "D"
                        DEC = DEC // 16
                        continue
                    elif DEC % 16 == 14:
                        ANS += "E"
                        DEC = DEC // 16
                        continue
                    elif DEC % 16 == 15:
                        ANS += "F"
                        DEC = DEC // 16
                        continue
                while DEC <=0:
                    break
                HEX=""
                for j in range(len(ANS)-1,-1,-1):
                    HEX+=ANS[j]
                print("Hexadecimal:", HEX)
            elif RUN!=len(BIN):
                print("Not Binary Number!")
        elif BIN == "-1":
            break
        else:
            print("Not Binary Number!")
fun_1()




