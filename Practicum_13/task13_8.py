def convert_date_time(str) -> None:
    try:
        date, time = str.split()
        month, day, year = map(int, date.split('/'))
        hour, minute, second = map(int, time.split(':'))
        
        if month < 1 or month > 12:
            print("Неверный месяц")

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29

        if day < 1 or day > days_in_month[month - 1]:
            print("Неверный день")
        if hour < 0 or hour > 23:
            print("Неверный час")
        if minute < 0 or minute > 59:
            print("Неверные минуты")
        if second < 0 or second > 59:
            print("Неверные секунды")
        
        period = "AM"
        display_hour = hour
        
        if hour == 0:
            display_hour = 12
        elif hour == 12:
            period = "PM"
        elif hour > 12:
            display_hour = hour - 12
            period = "PM"

        print(f"{day}.{month}.{year} {display_hour}:{minute}:{second} {period}")
        
    except ValueError:
        print("Ошибка: неверный формат")

date_input = input("Введите дату и время (MM/DD/YYYY HR:MIN:SEC): ")
convert_date_time(date_input)