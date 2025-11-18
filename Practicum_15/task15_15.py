def ten_to_bin(x: int) -> str:
    """
    Convert natural number from decimal to binary.
    
    Args:
        x: Natural number in decimal
    
    Returns:
        Binary representation as string
    """
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        return ten_to_bin(x // 2) + str(x % 2)


def main():
    """
    Main function to demonstrate the functionality of ten_to_bin.
    """
    x = int(input("Enter natural number: "))
    
    result = ten_to_bin(x)
    
    print(f"Binary: {result}")


if __name__ == '__main__':
    main()