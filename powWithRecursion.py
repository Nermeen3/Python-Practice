def myPow(x, n):
    if n == 0: return 1
    elif n < 0:
        #return (1 / (x * (myPow(x, -(n+1)))))
        return myPow(x, n+1) / x
    else:
        return x * (myPow(x, n-1))

print(myPow(2.0000, -2))
