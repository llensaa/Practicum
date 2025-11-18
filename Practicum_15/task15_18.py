def simmetr(s: str, i: int, j: int) -> bool:
    """
    Check if substring s[i:j+1] is symmetric.
    
    Args:
        s: Input string
        i: Start index
        j: End index
    
    Returns:
        True if substring is symmetric, False otherwise
    """
    if i >= j:
        return True
    elif s[i] != s[j]:
        return False
    else:
        return simmetr(s, i + 1, j - 1)


def main():
    """
    Main function to demonstrate the functionality of simmetr.
    """
    s = input("Enter string: ")
    i = int(input("Enter start index: "))
    j = int(input("Enter end index: "))
    
    result = simmetr(s, i, j)
    
    if result:
        print(f"Substring '{s[i:j+1]}' is symmetric")
    else:
        print(f"Substring '{s[i:j+1]}' is not symmetric")


if __name__ == '__main__':
    main()