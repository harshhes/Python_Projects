n = int(input("Enter a number: "))
flag =True
if n >1:
    for i in range(2, n//2+1):
        if n%i==0:
            flag =False
            break
    if flag:
        print("Prime")
    else:
        print("Not Prime")
else:
    print("Not Prime")
