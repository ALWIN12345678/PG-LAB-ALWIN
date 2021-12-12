s=int(input("Enter starting year"))
e=int(input("Enter ending year"))
if(s<e):
    print("leap years are",end=" ")
    for i in range(s,e):
        if(i%4==0 and i%100!=0 or i%400==0 and i%100==0):
            print(i,end=" ")