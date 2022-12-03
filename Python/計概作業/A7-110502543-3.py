tmp = []
def dfs(now, x) :
    global ans
    ans = ans[:now] + x + ans[now+1:]

    if (now == L-1):
        tmp.append(ans)

        return
    for i in range(len(arr[now+1])) :
        dfs(now+1, arr[now+1][i])
cin = open('digit.txt', 'r')
cout = open('110502543.txt', 'w')
s = cin.readline()
arr = []
L = len(s)
ans = '0'*L
for i in range(L) :
    if (s[i] == '1'):
        print("none\n110502543歐子謙",end='', file = cout)
        print("none\n110502543歐子謙",end='')
        exit()
    elif s[i] == '2' :
        arr.append("abc")
    elif s[i] == '3' :
        arr.append("def")
    elif s[i] == '4' :
        arr.append("ghi")
    elif s[i] == '5' :
        arr.append("jkl")
    elif s[i] == '6' :
        arr.append("mno")
    elif s[i] == '7' :
        arr.append("pqrs")
    elif s[i] == '8' :
        arr.append("tuv")
    else :
        arr.append("wxyz")
for i in range(len(arr[0])) :
    dfs(0, arr[0][i])
print(' '.join(tmp,),file=cout)
print(' '.join(tmp,))
print('110502543歐子謙',end='', file=cout)
print('110502543歐子謙',end='')
cin.close()
cout.close()
