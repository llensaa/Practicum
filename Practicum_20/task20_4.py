import re


class RomanNumber:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    def __init__(self, value):
        self.rom_value = None

        if isinstance(value, str) and self.is_roman(value):
            self.rom_value = value
        else:
            print('ошибка')

    @staticmethod
    def is_roman(value):
        pattern = r'^M{0,3}(CM|CD|D?C{0,3})' \
                  r'(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return isinstance(value, str) and re.fullmatch(pattern, value)

    def decimal_number(self):
        total = 0
        prev = 0

        # идём справа налево
        for ch in reversed(self.rom_value):
            val = self.roman_map[ch]

            if val < prev:
                total -= val
            else:
                total += val

            prev = val

        return total