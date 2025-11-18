def count(a: int, b: int) -> int:
    """
    Count how many squares can be cut from a rectangle a x b
    by always cutting the largest possible square.
    
    Args:
        a: Length of rectangle
        b: Width of rectangle
    
    Returns:
        Number of squares that can be cut
    """
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return 1
    elif a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)


def main():
    """
    Main function to demonstrate the functionality of count.
    """
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    result = count(a, b)
    
    print(f"Number of squares: {result}")


if __name__ == '__main__':
    main()