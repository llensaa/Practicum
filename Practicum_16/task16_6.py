def solve_equation() -> list:
    """
    Solve the puzzle HOD + HOD + HOD = MAT where each letter is a digit.
    
    Returns:
        List of all solutions as strings from smallest HOD to largest
    """
    solutions = []
    
    for hod in range(108, 1000):
        h = hod // 100
        o = (hod // 10) % 10
        d = hod % 10
        
        mat = hod * 3
        if mat >= 1000:
            break
        
        m = mat // 100
        a = (mat // 10) % 10
        t = mat % 10
        
        if len({h, o, d, m, a, t}) == 6:
            solutions.append(f"{hod} + {hod} + {hod} = {mat}")
    
    return solutions


def main():
    """
    Main function to demonstrate the functionality of solve_equation.
    """
    solutions = solve_equation()
    
    print("Все варианты расшифровки:")
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    main()