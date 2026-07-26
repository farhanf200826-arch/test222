def add():
    sum =0
    n = int(input("Number of integers you want to add:"))
    for i in range(n):
        x=int(input("enter the number :"))
        sum+=x
    print(sum)

add()