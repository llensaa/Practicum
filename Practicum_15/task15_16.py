def digit_to_char(d: int) -> str:
    """
    Convert digit to character for bases > 10.
    
    Args:
        d: Digit value (0-15)
    
    Returns:
        Character representation
    """
    if d < 10:
        return str(d)
    else:
        return chr(ord('A') + d - 10)


def ten_to_n(x: int, n: int) -> str:
    """
    Convert natural number from decimal to base n.
    
    Args:
        x: Natural number in decimal
        n: Target base (2-16)
    
    Returns:
        Number in base n as string
    """
    if x == 0:
        return ""
    else:
        remainder = x % n
        quotient = x // n
        if quotient == 0:
            return digit_to_char(remainder)
        else:
            return ten_to_n(quotient, n) + digit_to_char(remainder)


def main():
    """
    Main function to demonstrate the functionality of ten_to_n.
    """
    x = int(input("Enter natural number: "))
    n = int(input("Enter base (2-16): "))
    
    result = ten_to_n(x, n)
    
    print(f"Base {n}: {result}")


if __name__ == '__main__':
    main()