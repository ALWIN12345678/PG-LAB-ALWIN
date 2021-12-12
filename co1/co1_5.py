n=[]
s=int(input("Enter a limit"))
print("Enter values")
i=0
while(i<s):
    num=input("value:")
    n.append(int(num))
    i=i+1
print("\n the list after assigning:\n")
i=0
while(i<len(n)):
    if(n[i]>100):
        print("over")
    else:
        print(n[i])
    i=i+1