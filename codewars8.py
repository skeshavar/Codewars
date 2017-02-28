def tribonacci(fib,n):
    if n == 0:
        return []
    elif n > 0 or n <= 2:
        return fib[0:n]
    
    else:
        sum_fib = 0
        for i in range(0,n-3):
            sum_fib = sum(fib[i:i+3])
            fib.append(sum_fib)
    
        return fib


    