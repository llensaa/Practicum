def mod_number(a: int, b: int) -> int:
    """
    Find the remainder of division of natural number a by natural number b.
    
    Args:
        a: The dividend
        b: The divisor
    
    Returns:
        The remainder of a divided by b
    """
    if a == b or b == 1:
        return 0
    elif a < b:
        return a
    else:
        return mod_number(a - b, b)
    
def main():
    """
    Main function to demonstrate the functionality of mod_number.
    """
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))
    result = mod_number(a, b)
        
    print(f"The remainder of division of a by b = {result}")


if __name__ == '__main__':
    main()