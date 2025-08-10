n = int(input("Enter a number:  "))
a = 0
b = 1
print(f"Fibonacci sequence for {n} numbers is : \n")
print(f"{a} \n{b}", end=" ")
for i in range(n):
    c = a+b
    print(f"{c}", end=" ")
    a = b
    b = c
