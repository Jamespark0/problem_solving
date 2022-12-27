import numpy as np;

def fibonancci_bottom_up(n: int) -> int:
    # define a fucntion to store the values
    if n == 1 or n == 2:
        return 1;
    else:
        # create an numpy array to store the values
        fib = np.empty(shape= n + 1).astype(int);
        fib[1] = 1;
        fib[2] = 1;
        for i in range(3, n+1):
            fib[i] = fib[i - 1] + fib[i - 2];
        
        return fib[n];

print(fibonancci_bottom_up(1)); # 1
print(fibonancci_bottom_up(5)); # 5
print(fibonancci_bottom_up(10)); # 55
