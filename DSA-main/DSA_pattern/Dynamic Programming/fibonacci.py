# This code demonstrates the concept of dynamic programming by calculating the nth Fibonacci number using an iterative approach.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    


print(fibonacci(10))  # Output: 55


# List Append 
def append_to_list(n):
    
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:   
        fib_list = [0, 1]
        for _ in range(2, n + 1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        
        return fib_list

print(append_to_list(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]