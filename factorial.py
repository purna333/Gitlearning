n=5
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print("The Factorail of the number",n," is",fact(n))