def degree5(n: int) -> int:
    """
    Determine the exponent k such that 5 ** k = n.
    
    Args:
        n: A natural number to check if it is a power of 5
    
    Returns:
        The exponent k if n is a power of 5,
        or -1 if n is not a power of 5
    """
    if n > 0:
        if n == 1:
            return 0
        elif n % 5 != 0:
            return -1
        else:
            result = degree5(n // 5)
        if result == -1:
            return -1
        else:
            return 1 + result


def main():
    """
    Main function to demonstrate the functionality of degree5.
    """
    n = int(input("Enter a natural number: "))

    result = degree5(n)
        
    if result != -1:
        print(f"5 ** {result} = {n}")
    else:
        print(f"{n} is not a power of 5")


if __name__ == '__main__':
    main()