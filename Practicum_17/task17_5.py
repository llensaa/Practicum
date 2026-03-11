def build_family_tree(relations: list) -> dict:
    """
    Builds a family tree from parent-child relationships.
    
    Args:
        relations: List of strings with "parent child" relationships
    
    Returns:
        Dictionary with parent as key and list of children as value
    """
    tree = {}
    
    for relation in relations:
        parent, child = relation.split()
        
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
    
    return tree


def count_descendants(name: str, tree: dict) -> int:
    """
    Recursively counts all descendants (children, grandchildren, etc.) for a given name.
    
    Args:
        name: Name to count descendants for
        tree: Family tree dictionary
    
    Returns:
        Total number of descendants
    """
    if name not in tree:
        return 0
    
    total = 0
    for child in tree[name]:
        total += 1
        total += count_descendants(child, tree)
    
    return total


def main():
    """
    Main function to demonstrate counting descendants in a family tree.
    """
    n = int(input())
    relations = []

    for _ in range(n):
        relation = input()
        relations.append(relation)
    
    family_tree = build_family_tree(relations)
    name = input()
    result = count_descendants(name, family_tree)
    print(result)


if __name__ == '__main__':
    main()