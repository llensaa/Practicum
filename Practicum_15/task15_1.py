def pownum(a: int, n: int) -> int:
    """
    Calculate the exponent k such that (a ** k = n) or returns "n is nor a power of a".
    
    Args:
        a: The base number
        n: The number to check the power of a
    
    Returns:
        The exponent k such that a ** k = n
    """
    if n == 1:
        return 0
    else:
        return 1 + pownum(a, (n // a))
    
def main():
    """
    Main function to demonstrate the functionality of pownum.
    """
    a = int(input("Enter a: "))
    n = int(input("Enter n: "))
    result = pownum(a, n)
        
    print(f"{a} ** {result} = {n}")


if __name__ == '__main__':
    main()