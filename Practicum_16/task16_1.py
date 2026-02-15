def repeating(numbers_str: str, target: int) -> bool:
    """
    Check if the target number belongs to the set of repeating numbers.
    
    Args:
        numbers_str: String with space-separated natural numbers
        target: Number to check
    
    Returns:
        True if target is a repeating number, False otherwise
    """
    numbers = list(map(int, numbers_str.split()))
    counts = {}
    
    for num in numbers:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
    
    repeating_numbers = {num for num, count in counts.items() if count > 1}
    
    return target in repeating_numbers


def main():
    """
    Main function to demonstrate the functionality of repeating.
    """
    numbers_str = input("Введите последовательность чисел: ")
    target = int(input("Введите число: "))
    
    result = repeating(numbers_str, target)
    
    if result:
        print(f"{target} принадлежит множеству повторяющихся чисел")
    else:
        print(f"{target} не принадлежит множеству повторяющихся чисел")


if __name__ == '__main__':
    main()