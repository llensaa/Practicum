class MorseMsg:
    """Класс, представляющий сообщение на азбуке Морзе."""
    
    # Словарь для декодирования (латиница)
    morse_to_eng = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
    
    # Словарь для декодирования (кириллица)
    morse_to_ru = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '.-.-': 'Э',
        '..--': 'Ю', '.-.-.': 'Я'
    }
    
    # Гласные буквы
    vowels_eng = set('AEIOU')
    vowels_ru = set('АЕЁИОУЫЭЮЯ')
    
    def __init__(self, encoded_msg):
        """
        Инициализация сообщения.
        
        Параметры:
        encoded_msg - строка с закодированным сообщением
        """
        self.encoded_msg = encoded_msg
        self.morse_words = encoded_msg.split(' ')
    
    def eng_decode(self):
        """Декодирует сообщение на латинице."""
        result = ''
        for morse in self.morse_words:
            if morse in self.morse_to_eng:
                result += self.morse_to_eng[morse]
        return result
    
    def ru_decode(self):
        """Декодирует сообщение на кириллице."""
        result = ''
        for morse in self.morse_words:
            if morse in self.morse_to_ru:
                result += self.morse_to_ru[morse]
        return result
    
    def get_vowels(self, lang):
        """Возвращает список гласных букв в порядке следования."""
        if lang == 'eng':
            decoded = self.eng_decode()
            return [ch for ch in decoded if ch in self.vowels_eng]
        else:
            decoded = self.ru_decode()
            return [ch for ch in decoded if ch in self.vowels_ru]
    
    def get_consonants(self, lang):
        """Возвращает список согласных букв в порядке следования."""
        if lang == 'eng':
            decoded = self.eng_decode()
            return [ch for ch in decoded if ch not in self.vowels_eng]
        else:
            decoded = self.ru_decode()
            return [ch for ch in decoded if ch not in self.vowels_ru]
    
    def __str__(self):
        """Строковое представление сообщения."""
        return f"MorseMsg('{self.encoded_msg}')"
