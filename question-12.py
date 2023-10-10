tnum=1
i=2

while True:
    tnum+=i
    i+=1
    
    count=0
    for j in range(1, int(tnum**0.5)+1):
        if tnum % j == 0:
            count+=2
            
    if int(tnum**0.5)**2 == tnum:
        count -= 1
        
    if count>500:
        print(tnum)
        break
