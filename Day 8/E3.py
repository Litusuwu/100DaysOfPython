def prime_checker(number):
    prime = [True for i in range(number+1)]
    p = 2
    while p*p <= number:
        if prime[p] :
            for i in range ( p*p, number+1, p):
                prime[i]=False
        p+=1
    
    if prime[number]:
        print("Is a prime number")
    else:
        print("Is not a prime number")


n = int(input())
prime_checker(number=n)