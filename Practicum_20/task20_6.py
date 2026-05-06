import re


class RomanNumber:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    int_map = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    def __init__(self, value):
        self.rom_value = None
        self.int_value = None

        if isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self.to_int(value)
            else:
                print('ошибка')

        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self.to_roman(value)
            else:
                print('ошибка')

    @staticmethod
    def is_roman(value):
        pattern = r'^M{0,3}(CM|CD|D?C{0,3})' \
                  r'(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return isinstance(value, str) and re.fullmatch(pattern, value)

    @staticmethod
    def is_int(value):
        return isinstance(value, int) and 0 < value < 4000

    def to_int(self, roman):
        total = 0
        prev = 0
        for ch in reversed(roman):
            val = self.roman_map[ch]
            total += val if val >= prev else -val
            prev = val
        return total

    def to_roman(self, num):
        res = ''
        for val, sym in self.int_map:
            while num >= val:
                res += sym
                num -= val
        return res

    @staticmethod
    def error():
        obj = RomanNumber(1)
        obj.int_value = None
        obj.rom_value = None
        return obj

    def __repr__(self):
        return str(self.rom_value)

    def _check(self, value):
        return self.is_int(value)

    def _make(self, value):
        return RomanNumber(value)

    def __add__(self, other):
        res = self.int_value + other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __sub__(self, other):
        res = self.int_value - other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __mul__(self, other):
        res = self.int_value * other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __truediv__(self, other):
        if other.int_value == 0 or self.int_value % other.int_value != 0:
            print('ошибка')
            return self.error()
        return RomanNumber(self.int_value // other.int_value)

    def __floordiv__(self, other):
        res = self.int_value // other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __mod__(self, other):
        res = self.int_value % other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __pow__(self, other):
        res = self.int_value ** other.int_value
        return self._make(res) if self._check(res) else self.error()

    def __iadd__(self, other):
        return self.__assign(self.__add__(other))

    def __isub__(self, other):
        return self.__assign(self.__sub__(other))

    def __imul__(self, other):
        return self.__assign(self.__mul__(other))

    def __itruediv__(self, other):
        return self.__assign(self.__truediv__(other))

    def __ifloordiv__(self, other):
        return self.__assign(self.__floordiv__(other))

    def __imod__(self, other):
        return self.__assign(self.__mod__(other))

    def __ipow__(self, other):
        return self.__assign(self.__pow__(other))

    def __assign(self, obj):
        self.int_value = obj.int_value
        self.rom_value = obj.rom_value
        return self