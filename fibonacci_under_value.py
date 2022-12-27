# Problem 2 from project Euler: Even Fibonacci numbers
import numpy as np;

def fibonacci_under(n: int) -> np.ndarray:
    fib = {1: 1, 2: 1};

    # the index starts from 3
    index: int = 3;
    # init the buffer value for the next slot
    buffer = fib[1] + fib[2];

    while buffer <= n:
        fib[index] = buffer;
        index += 1;
        buffer = fib[index - 1] + fib[index - 2];

    return np.array(list(fib.values()))

# store the sequence below the given number
num = 4_000_000
fib_sequence = fibonacci_under(num);
# sum the even values
even_sum = np.sum(fib_sequence[np.where(fib_sequence % 2 == 0)]);

print(even_sum)