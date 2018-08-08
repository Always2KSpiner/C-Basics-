def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
    else:
        print(num,"is not a prime number")
def is_even(num):
    if(num%2==0):
        print(num," IS EVEN")
    else:
        print(num," IS ODD")