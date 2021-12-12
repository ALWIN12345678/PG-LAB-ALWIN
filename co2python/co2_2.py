#fibonacci series
n=int(input("Enter limit"))
a=0
b=1
sum=0
print("Fibonacci series:",end=" ")
i=1
while(i<=n):
    print(sum,end=" ")
    a=b
    b=sum
    sum=a+b
    i=i+1