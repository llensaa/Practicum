class Lesson:
    def __init__(self, teacher, subject, group, room, day):
        self._teacher = teacher
        self._subject = subject
        self._group = group
        self._room = room
        self._day = day

    def get_group(self):
        return self._group

    def __str__(self):
        return f"{self._day}: {self._subject} ({self._teacher}) ауд. {self._room}"
    

class Schedule:
    def __init__(self):
        self._lessons = []

    def add_lesson(self, lesson: Lesson):
        self._lessons.append(lesson)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                teacher, subject, group, room, day = line.strip().split(",")
                lesson = Lesson(teacher, subject, int(group), room, day)
                self.add_lesson(lesson)

    def get_group_schedule(self, group_number):
        result = []
        for lesson in self._lessons:
            if lesson.get_group() == group_number:
                result.append(lesson)
        return result

    def print_group_schedule(self, group_number):
        lessons = self.get_group_schedule(group_number)

        if not lessons:
            print("Расписание не найдено")
            return

        print(f"Расписание группы {group_number}:\n")
        for lesson in lessons:
            print(lesson)


schedule = Schedule()
schedule.load_from_file("Practicum/Practicum_21/task21_4/schedule.txt")
group = 24704
schedule.print_group_schedule(group)
