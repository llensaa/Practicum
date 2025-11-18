def primes(x: int, divisor: int) -> int:
    """
    Check if x is prime by testing divisors.
    
    Args:
        x: Number to check
        divisor: Current divisor to test
    
    Returns:
        1 if prime, 0 if not prime
    """
    if divisor > x ** 0.5:
        return 1
    elif x % divisor == 0:
        return 0
    else:
        return primes(x, divisor + 2)


def function1(x: int) -> int:
    """
    Check if natural number x is prime.
    
    Args:
        x: Natural number to check
    
    Returns:
        1 if x is prime, 0 otherwise
    """
    if x < 2:
        return 0
    elif x == 2:
        return 1
    elif x % 2 == 0:
        return 0
    else:
        return primes(x, 3)


def main():
    """
    Main function to demonstrate the functionality of function1.
    """
    x = int(input("Enter natural number: "))
    
    result = function1(x)
    
    if result == 1:
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime")


if __name__ == '__main__':
    main()