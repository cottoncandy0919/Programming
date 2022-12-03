"""
Assignment 7
Name:歐子謙
Student Number:110502543
Course 2021-CE1003-B
"""
FILE=open('seat.txt','r')
list=FILE.readlines()
seat=list[0]
ANS=''
x=0
seatarr=[]
interval=[]
Myseat=[]
onlyONE=[]
endpoint=[]
criticalpoint=[]
if seat.count('1')==1:
    for i in range(len(seat)):
        x+=1
        if seat[i] == '1':
            x = i
            seatarr.append(x)
    ans1=int(seatarr[0])-int(seat[0])
    ans2=int((len(seat)-1))-int(seatarr[0])
    if ans1 == ans2 and seat[0]=='0'and seat[len(seat)-1]:
        print('L =',int(len(seat)) - 1 - int(seatarr[0]),',i =','0 ,',int(len(seat))-1)
    elif ans1 == ans2:
        print('L =',int(len(seat)) - 1 - int(seatarr[0]),',i =',int(len(seat)) - 1)
    elif ans1 > ans2:
        print('L =',int(seatarr[0]) - int(seat[0]),',i =','0')
    else:
        print('L =',int((len(seat) - 1)) - int(seatarr[0]),',i =',int(len(seat)) - 1)
else:
    for i in range(len(seat)):
        x+=1
        if seat[i]=='1':
            x=i
            seatarr.append(x)
    if seat[0] == '0':
        endpoint.append(0)
        endpoint_LMAX = seatarr[0] - endpoint[0]
        interval.append(endpoint_LMAX)
    if seat[len(seat)-1]=='0':
        endpoint.append(len(seat)-1)
        endpoint_RMAX = endpoint[len(endpoint) - 1] - seatarr[len(seatarr) - 1]
        interval.append(endpoint_RMAX)
    for i in range(len(seatarr)):
        intervalnum = 0
        if i ==len(seatarr)-1:
            continue
        else:
            intervalnum = -seatarr[i]+seatarr[i+1]
            interval.append(intervalnum//2)
            criticalpoint.append(intervalnum//2)
    MAX=max(interval)
    #print(MAX)
    if seat[0]=='0':
        if MAX== endpoint_LMAX:
            Myseat.append(0)
    if seat[len(seat)-1]=='0':
        if MAX == endpoint_RMAX:
            Myseat.append(len(seat)-1)
    if criticalpoint.count(MAX)>=1:
        for k in range(len(seatarr)):
            if k == len(seatarr) - 1:
                continue
            else:
                a = (-seatarr[k] + seatarr[k + 1])//2
                if a==MAX:
                    if ((seatarr[k] + seatarr[k + 1])/2)%1!=0:
                        myseat = (seatarr[k] + seatarr[k + 1]) // 2
                        myseat2=myseat+1
                        Myseat.append(myseat)
                        Myseat.append(myseat2)
                    else:
                        myseat = (seatarr[k] + seatarr[k + 1]) // 2
                        Myseat.append(myseat)
    print('L =',MAX,',i =',str(sorted(Myseat))[1:-1])
FILE.close()