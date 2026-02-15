def sieve_of_eratosthenes(n: int) -> set:
    """
    Find all prime numbers less than n using the Sieve of Eratosthenes.
    
    Args:
        n: Upper bound
    
    Returns:
        Set of prime numbers less than n
    """
    if n <= 2:
        return set()
    
    numbers = set(range(2, n))
    
    for i in range(2, int(n ** 0.5) + 1):
        multiples = set(range(i * i, n, i))
        numbers -= multiples
    
    return numbers


def main():
    """
    Main function to demonstrate the functionality of sieve_of_eratosthenes.
    """
    n = int(input("Введите n: "))
    
    primes = sieve_of_eratosthenes(n)
    
    sorted_primes = sorted(primes)
    print(f"Простые числа меньше {n}: {sorted_primes}")


if __name__ == '__main__':
    main()