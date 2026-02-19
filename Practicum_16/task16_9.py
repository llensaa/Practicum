from itertools import combinations


def get_k_subsets(numbers_str: str, K: int) -> list:
    """
    Get all K-element subsets of the given set.
    
    Args:
        numbers_str: String with space-separated natural numbers
        K: Size of subsets
    
    Returns:
        List of all K-element subsets
    """
    numbers = list(map(int, numbers_str.split()))
    numbers.sort()
    
    if K < 0:
        return []
    
    k_subsets = [list(combo) for combo in combinations(numbers, K)]
    
    return k_subsets


def main():
    """
    Main function to demonstrate the functionality of get_k_subsets.
    """
    numbers_str = input("Введите множество чисел: ")
    K = int(input("Введите K: "))
    
    k_subsets = get_k_subsets(numbers_str, K)
    
    print(f"Все {K}-элементные подмножества:")
    for subset in k_subsets:
        print(subset)


if __name__ == '__main__':
    main()
