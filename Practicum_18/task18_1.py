def count_uppercase_in_range(s: str, i: int, j: int) -> int:
    """
    Counts uppercase characters in a string from position i to j inclusive.
    
    Args:
        s: Input string
        i: Starting position (1-based index)
        j: Ending position (1-based index)
    
    Returns:
        Number of uppercase characters in the specified range
    """
    substring = s[i-1:j]
    uppercase_chars = list(filter(lambda ch: ch.isupper(), substring))
    return len(uppercase_chars)


def main():
    """
    Main function to demonstrate uppercase character counting.
    """
    s = input("Enter string: ")
    i = int(input("i = "))
    j = int(input("j = "))
    
    result = count_uppercase_in_range(s, i, j)
    print(result)


if __name__ == '__main__':
    main()