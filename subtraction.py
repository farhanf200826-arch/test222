def subtraction():
    n = int(input("enter the number of integers:"))
    final = int(input("enter the biggest number"))
    for i in range(n-1):
        x = int(input("enter the remaining numbers(desc order):"))
        final-=x
    print(final)

subtraction()