def multiply():
    final =1
    n = int(input("enter number of integers you want to multiply:"))
    for i in range(n):
        x =int(input("enter the number:"))
        final*=x
    print(final)

multiply()