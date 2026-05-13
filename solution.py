PRODUCT_DATA = {
    "460": {"country": "Россия", "name": "Товар РФ"},
    "400": {"country": "Германия", "name": "Товар DE"},
    "590": {"country": "Польша", "name": "Товар PL"},
    "000": {"country": "Неизвестно", "name": "Товар"}
}


class Product:
    def __init__(self, barcode, price):
        self._barcode = barcode
        self._price = price

        prefix = barcode[:3]
        self._country = PRODUCT_DATA.get(prefix, {}).get("country", "Unknown")

    def get_barcode(self):
        return self._barcode

    def get_price(self):
        return self._price

    def get_country(self):
        return self._country

    def set_price(self, value):
        if value >= 0:
            self._price = value

    def __str__(self):
        return f"{self._barcode} | {self._country} | {self._price}₽"


class Cart:
    def __init__(self):
        self._products = []
        self._total_price = 0

    def get_total_price(self):
        return self._total_price

    def get_products(self):
        return self._products

    def _recalc(self):
        self._total_price = sum(p.get_price() for p in self._products)

    def add_product(self, product):
        self._products.append(product)
        self._recalc()

    def remove_product(self, barcode):
        for p in self._products:
            if p.get_barcode() == barcode:
                self._products.remove(p)
                self._recalc()
                return True
        return False

    def __str__(self):
        if not self._products:
            return "Корзина пуста"

        result = "Корзина:\n"
        for p in self._products:
            result += str(p) + "\n"
        result += f"Итого: {self._total_price}₽"
        return result


def load_products(filename):
    products = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            barcode, price = line.strip().split(",")
            products.append(Product(barcode, float(price)))
    return products


def menu():
    cart = Cart()
    products = []

    while True:
        print("\n1. Загрузить товары")
        print("2. Добавить товар в корзину")
        print("3. Удалить товар из корзины")
        print("4. Показать корзину")

        choice = input("Выбор: ")

        if choice == "1":
            filename = input("Файл: ")
            products = load_products(filename)
            print("Загружено")

        elif choice == "2":
            barcode = input("Штрих-код: ")
            for p in products:
                if p.get_barcode() == barcode:
                    cart.add_product(p)
                    print("Добавлено")
                    break

        elif choice == "3":
            barcode = input("Штрих-код: ")
            if cart.remove_product(barcode):
                print("Удалено")
            else:
                print("Не найдено")

        elif choice == "4":
            print(cart)


if __name__ == "__main__":
    menu()