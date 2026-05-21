from datetime import datetime


class Date:
    def __init__(self, date_string):
        self._date = None
        self.date = date_string

    @property
    def date(self):
        if self._date is None:
            return None
        months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн',
                  'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
        day = self._date.day
        month_name = months[self._date.month - 1]
        year = self._date.year
        return f"{day} {month_name} {year} г."

    @date.setter
    def date(self, value):
        try:
            day, month, year = map(int, value.split('.'))
            datetime(year, month, day)
            self._date = datetime(year, month, day)
        except (ValueError, AttributeError):
            print('ошибка')
            self._date = None

    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return self._date == other._date

    def __str__(self):
        if self._date is None:
            return 'None'
        return self.date


class User:
    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        self.id = int(id)
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):
        name_parts = []
        if self.first_name:
            name_parts.append(self.first_name)
        if self.last_name:
            name_parts.append(self.last_name)
        if self.middle_name:
            name_parts.append(self.middle_name)

        full_name = ' '.join(name_parts) if name_parts else ''

        result = f"ID: {self.id} LOGIN: {self.nick_name} NAME: {full_name}"
        if self.gender:
            result += f" GENDER: {self.gender}"
        return result


class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = int(id)
        self.date = Date(date)
        self.title = title
        self.employees = []

    def add_person(self, person):
        """Добавляет сотрудника в список participants"""
        if person not in self.employees:
            self.employees.append(person)

    def count(self):
        """Возвращает количество участников встречи"""
        return len(self.employees)

    def __str__(self):
        result = f"{self.title}\n{self.date}\n"
        for employee in self.employees:
            result += f"{employee}\n"
        return result.rstrip('\n')

    @classmethod
    def total(cls):
        """Возвращает общее количество участников всех встреч"""
        total_count = 0
        for meeting in cls.lst_meeting:
            total_count += meeting.count()
        return total_count

    @classmethod
    def count_meeting(cls, date):
        """Возвращает количество встреч в указанную дату"""
        count = 0
        for meeting in cls.lst_meeting:
            if meeting.date == date:
                count += 1
        return count


class Load:
    @staticmethod
    def write(meetings_file, persons_file, pers_meetings_file):
        """Загружает данные из файлов и создает объекты Meeting"""
        Meeting.lst_meeting = []

        users = {}

        try:
            with open(persons_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    # Пропускаем заголовок
                    for line in lines[1:]:
                        line = line.strip()
                        if not line:
                            continue

                        values = [v.strip() for v in line.rstrip(';').split(';')]

                        if len(values) >= 6:
                            user = User(
                                id=values[0],
                                nick_name=values[1],
                                first_name=values[2],
                                last_name=values[3],
                                middle_name=values[4],
                                gender=values[5]
                            )
                            users[user.id] = user
        except FileNotFoundError:
            print(f"Файл {persons_file} не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла {persons_file}: {e}")

        meetings_dict = {}
        try:
            with open(meetings_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    for line in lines[1:]:
                        line = line.strip()
                        if not line:
                            continue

                        values = [v.strip() for v in line.rstrip(';').split(';')]

                        if len(values) >= 3:
                            meeting = Meeting(
                                id=values[0],
                                date=values[1],
                                title=values[2]
                            )
                            meetings_dict[meeting.id] = meeting
                            Meeting.lst_meeting.append(meeting)
        except FileNotFoundError:
            print(f"Файл {meetings_file} не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла {meetings_file}: {e}")

        try:
            with open(pers_meetings_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    # Пропускаем заголовок
                    for line in lines[1:]:
                        line = line.strip()
                        if not line:
                            continue

                        values = [v.strip() for v in line.rstrip(';').split(';')]

                        if len(values) >= 2:
                            meet_id = int(values[0])
                            pers_id = int(values[1])

                            if meet_id in meetings_dict and pers_id in users:
                                meetings_dict[meet_id].add_person(users[pers_id])
        except FileNotFoundError:
            print(f"Файл {pers_meetings_file} не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла {pers_meetings_file}: {e}")

        return Meeting.lst_meeting