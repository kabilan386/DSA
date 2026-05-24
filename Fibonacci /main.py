def climbStairs(n):

    # if n <= 2:
    #     return n

    a = 0
    b = 1

    for _ in range(3, n + 1):
        print(a)
        c = a + b
        a = b
        b = c
    
  
    print(b)
    return b

climbStairs(30)