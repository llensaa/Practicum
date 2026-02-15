def in_intersection(set1_str: str, set2_str: str, value: int) -> bool:
    """
    Check if value belongs to the intersection of two sets.
    
    Args:
        set1_str: String with elements of first set
        set2_str: String with elements of second set
        value: Value to check
    
    Returns:
        True if value is in intersection, False otherwise
    """
    set1 = set(map(int, set1_str.split()))
    set2 = set(map(int, set2_str.split()))
    
    intersection = set1 & set2
    
    return value in intersection


def main():
    """
    Main function to demonstrate the functionality of in_intersection.
    """
    set1_str = input("Введите элементы первого множества: ")
    set2_str = input("Введите элементы второго множества: ")
    value = int(input("Введите значение для проверки: "))
    
    result = in_intersection(set1_str, set2_str, value)
    
    if result:
        print(f"{value} принадлежит пересечению множеств")
    else:
        print(f"{value} не принадлежит пересечению множеств")


if __name__ == '__main__':
    main()