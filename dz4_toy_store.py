class Product:
    def __init__(self, name, category, price, stock_quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.price = new_price

    def change_stock(self, amount):
        if self.stock_quantity + amount < 0:
            raise ValueError(f"Недостатньо товару '{self.name}' на складі")
        self.stock_quantity += amount

    def __repr__(self):
        return f"Product({self.name}, {self.price}грн, {self.stock_quantity}шт)"


class Order:
    def __init__(self):
        self.items = []
        self.total_amount = 0.0

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Кількість повинна бути більшою за нуль")
        if quantity > product.stock_quantity:
            raise ValueError(f"Недостатньо товару '{product.name}' на складі")

        product.change_stock(-quantity)
        self.items.append((product, quantity))
        self.calculate_total()

    def calculate_total(self):
        self.total_amount = sum(p.price * qty for p, qty in self.items)
        return self.total_amount

    def __repr__(self):
        items_str = ", ".join(f"{p.name} x{qty}" for p, qty in self.items)
        return f"Order([{items_str}], total={self.total_amount}грн)"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __repr__(self):
        return f"Customer({self.name}, {self.email}, orders={len(self.orders)})"


def load_store(filename):
    products = []
    customers = []
    current_section = None

    with open(filename, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()

            if not line:
                continue

            if line == "[PRODUCTS]":
                current_section = "products"
                continue
            elif line == "[CUSTOMERS]":
                current_section = "customers"
                continue

            try:
                if current_section == "products":
                    name, category, price, quantity = line.split(";")
                    products.append(Product(name, category, price, quantity))
                elif current_section == "customers":
                    name, email = line.split(";")
                    customers.append(Customer(name, email))
            except ValueError:
                print(f"Пропущено некоректний рядок {line_num}: {line}")

    return products, customers




# --- Основна програма ---

products, customers = load_store("store.txt")

print("--- Товари в магазині ---")
for p in products:
    print(p)

print("\n--- Клієнти магазину ---")
for c in customers:
    print(c)

# Звичайний клієнт з замовленням
customer = customers[0]
order = Order()
order.add_product(products[0], 2)   # 2 ведмедики
order.add_product(products[1], 1)   # 1 конструктор
customer.add_order(order)

print("\n--- Результат замовлення ---")
print(f"Клієнт: {customer.name} ({customer.email})")
print(f"Замовлені товари: {[(p.name, qty) for p, qty in order.items]}")
print(f"Загальна сума замовлення: {order.total_amount} грн")

# Клієнт без жодного замовлення
customer_no_orders = customers[2]
print(f"\n--- Клієнт без замовлень ---")
print(f"{customer_no_orders.name} має {len(customer_no_orders.orders)} замовлень")

# Спроба замовити товар, якого немає в наявності
print("\n--- Спроба замовити товар з нульовим залишком ---")
puzzle = products[3]
try_order = Order()
try:
    try_order.add_product(puzzle, 1)
except ValueError as e:
    print(f"Помилка: {e}")

print("\n---Залишки на складі після всіх операцій---")
for p in products:
    print(p)