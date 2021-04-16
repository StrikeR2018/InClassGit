def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i),
        i = i + 1
         
a = int(input("Enter a number to find its divisors："))
printDivisors(a)