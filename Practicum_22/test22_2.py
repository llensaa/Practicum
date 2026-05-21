import calendar
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

    def to_timestamp(self):
        if self._date is None:
            return None
        return int(calendar.timegm(self._date.timetuple()))

    def __lt__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return False
        return self._date < other._date

    def __le__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return False
        return self._date <= other._date

    def __gt__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return False
        return self._date > other._date

    def __ge__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return False
        return self._date >= other._date

    def __eq__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return False
        return self._date == other._date

    def __ne__(self, other):
        if not isinstance(other, Date) or self._date is None or other._date is None:
            return True
        return self._date != other._date

    def __str__(self):
        if self._date is None:
            return 'None'
        return self.date