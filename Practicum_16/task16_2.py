def unique_courses_count(N: int, courses_list: list) -> int:
    """
    Determine how many unique courses were selected by all students.
    
    Args:
        N: Number of students
        courses_list: List of strings with courses for each student
    
    Returns:
        Number of unique courses
    """
    all_courses = " ".join(courses_list).split()
    unique_courses = set(all_courses)
    
    return len(unique_courses)


def main():
    """
    Main function to demonstrate the functionality of unique_courses_count.
    """
    N = int(input("Введите количество студентов: "))
    courses_list = []
    
    for i in range(N):
        courses = input(f"Введите курсы для студента {i + 1}: ")
        courses_list.append(courses)
    
    result = unique_courses_count(N, courses_list)
    
    print(f"Количество уникальных курсов: {result}")


if __name__ == '__main__':
    main()