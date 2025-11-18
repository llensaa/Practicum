def nod(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two natural numbers a and b.
    
    Args:
        a: First natural number
        b: Second natural number
    
    Returns:
        The greatest common divisor of a and b
    """
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def main():
    """
    Main function to demonstrate the functionality of nod.
    """
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = nod(a, b)
    
    print(f"The greatest common divisor of {a} and {b} is {result}")


if __name__ == '__main__':
    main()