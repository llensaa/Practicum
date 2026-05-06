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
                self.int_value = self.decimal_number()
            else:
                print('ошибка')

        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self.roman_number()
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

    def decimal_number(self):
        total = 0
        prev = 0

        for ch in reversed(self.rom_value):
            val = self.roman_map[ch]
            total += val if val >= prev else -val
            prev = val

        return total

    def roman_number(self):
        num = self.int_value
        result = ''

        for val, sym in self.int_map:
            while num >= val:
                result += sym
                num -= val

        return result