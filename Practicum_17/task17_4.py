def create_form_dictionary(lines: list) -> dict:
    """
    Creates a dictionary mapping objects to their forms.
    
    Args:
        lines: List of strings where first word is form, following words are objects
    
    Returns:
        Dictionary with objects as keys and their forms as values
    """
    forms = {}
    
    for line in lines:
        words = line.split()
        form = words[0]
        objects = words[1:]
        
        for obj in objects:
            forms[obj] = form
    
    return forms


def find_form(obj: str, forms: dict) -> str:
    """
    Finds the form of an object using the provided dictionary.
    If the object is not found in the dictionary, it remains unchanged.
    
    Args:
        obj: Object to find form for
        forms: Dictionary mapping objects to their forms
    
    Returns:
        Form of the object if found, otherwise the original object
    """
    if obj in forms:
        return forms[obj]
    else:
        return obj


def main():
    """
    Main function to demonstrate form lookup.
    """
    n = int(input())
    lines = []

    for _ in range(n):
        line = input()
        lines.append(line)
    
    forms = create_form_dictionary(lines)
    obj = input()
    result = find_form(obj, forms)
    print(result)


if __name__ == '__main__':
    main()