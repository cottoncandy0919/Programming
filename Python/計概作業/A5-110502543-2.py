"""
Assignment 5
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
while 1:
    Input = input()
    if Input.count("+") == 1:
        if Input != "-1":
            BIN=Input.split("+")
            LBIN=BIN[0]
            RBIN=BIN[1]
            LDEC=0
            RDEC=0
            for i in range(len(LBIN)):
                LDEC+=int(LBIN[i])*2**(len(LBIN)-1-i)
            for j in range(len(RBIN)):
                RDEC+=int(RBIN[j])*2**(len(RBIN)-1-j)
            SUM=LDEC+RDEC
            ANS=0
            x=0#次方
            while 1:
                if SUM>0:
                    ANS+=SUM%2*10**x
                    SUM=SUM//2
                    x+=1
                elif SUM == 0:
                    break
        elif Input=="-1":
            break
        print(ANS)
    elif Input.count("-") == 1 and Input[0] != "-":
        BIN = Input.split("-")
        LBIN = BIN[0]
        RBIN = BIN[1]
        LDEC = 0
        RDEC = 0
        for i in range(len(LBIN)):
            LDEC += int(LBIN[i]) * 2 ** (len(LBIN) - 1 - i)
        for j in range(len(RBIN)):
            RDEC += int(RBIN[j]) * 2 ** (len(RBIN) - 1 - j)
        SUM = LDEC - RDEC
        ANS = 0
        x = 0  # 次方
        while 1:
            if SUM > 0:
                ANS += SUM % 2 * 10 ** x
                SUM = SUM // 2
                x += 1
            elif SUM == 0:
                break
        print(ANS)
    else:
        break
