def fib(k: int) -> int:
    """
    Compute the k-th term of the Fibonacci sequence.
    
    Args:
        k: The position in Fibonacci sequence
    
    Returns:
        The k-th Fibonacci number
    """
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


def main():
    """
    Main function to demonstrate the functionality of fib.
    """
    k = int(input("Enter k: "))
    
    result = fib(k)
    
    print(f"fib({k}) = {result}")


if __name__ == '__main__':
    main()