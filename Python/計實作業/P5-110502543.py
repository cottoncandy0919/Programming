"""
Practice 5
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
def _2to_10():
    while 1:
        BIN = input('NUM(BIN) : ')
        if BIN != "-1":
            NUM_DEC = 0
            RUN = BIN.count('0') + BIN.count('1')
            if RUN == len(BIN):
                for i in range(len(BIN)):
                    DEC = int(BIN[i]) * 2 ** (len(BIN) - 1 - i)
                    NUM_DEC += DEC
                print("NUM(DEC) after X16 ：", NUM_DEC * 16)
                x = 0
                OCT = 0
                T=NUM_DEC*16
                while T > 0:
                    OCT_1 = T % 8 * (10 ** x)
                    T = T // 8
                    x += 1
                    OCT += OCT_1
                while T <= 0:
                    break
                print("NUM(OCT) :", OCT)
            if RUN != len(BIN):
                print("Not Binary Number ！")
        elif BIN == "-1":
            break
        print("")
_2to_10()







