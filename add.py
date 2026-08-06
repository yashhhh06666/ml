def add(n):
   
    if n == 0:
        return 0
    else:
        return n+add(n-1) 

n = int(input("enter a number: "))
z = add(n)

print(z)
