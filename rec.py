# def fact(n):
   
#     if n == 0:
#         return 1
#     return n * fact(n - 1)


# if __name__ == "__main__":
#     number = int(input("enter a number: "))
#     print(f"{number}! = {fact(number)}")

# ---------------------------

# recursion with loop 

def Fact(n):
    if n== 0:
        return 1
    else:
        return n * Fact(n-1)
