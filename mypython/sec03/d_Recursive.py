def factorial(n):
    print(f'--------{n}')
    if n==0:
        return 1
    else:
        return n*factorial(n-1) #5*factorial(4)
                                #      4* factorial(3)
                                #              3* factorial(2)
                                #                       2* factorial(1)
                                #                               1*factorial(0)
                                #                                   return 1 = 5*4*3*2*1*1 = 5!

if __name__ == '__main__':
    print(factorial(5))