def sort_words_by_frequency(text: str) -> str:
    """
    Returns words from the string sorted by decreasing frequency of occurrence.
    
    Args:
        text: Input string with space-separated words
    
    Returns:
        String with words sorted by decreasing frequency
    """
    words = text.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    
    sorted_words = sorted(frequency.keys(), 
                         key=lambda x: frequency[x], 
                         reverse=True)
    
    return ' '.join(sorted_words)


def main():
    """
    Main function to demonstrate the program functionality.
    """
    text = input()
    result = sort_words_by_frequency(text)
    print(result)


if __name__ == '__main__':
    main()