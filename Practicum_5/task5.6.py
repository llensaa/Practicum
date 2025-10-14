first_day = int(input())
second_day = int(input())
third_day = int(input())
if first_day == second_day == third_day:
    print("3")
elif first_day != second_day and second_day != third_day and first_day != third_day:
    print("1")
else:
    print("2")