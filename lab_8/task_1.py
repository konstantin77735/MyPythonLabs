#онлайн-магазин
class OnlineStore:
    def __init__(self):
        self.customers = {}  # Словарь для хранения информации о клиентах
        self.products = {}   # Словарь для хранения информации о продуктах
        self.orders = {}     # Словарь для хранения заказов
        self.next_order_id = 1  # Начальное значение номера заказа

    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.customers[email] = customer

    def add_product(self, name, price):
        product = Product(name, price)
        self.products[name] = product

    def display_customers(self):
        print("Список клиентов:")
        for customer in self.customers.values():
            print(customer)

    def display_products(self):
        print("Список продуктов:")
        for product in self.products.values():
            print(product)

#товар
class Product(OnlineStore):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price}"

#заказ
class Order(Product):
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def calculate_total_amount(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Заказ от {self.customer.name}: {self.product.name} ({self.quantity} шт.), Сумма: {self.calculate_total_amount()}"

#покупатель
class Customer(Order):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Имя: {self.name}, Email: {self.email}"

#класс обрабатывает поступающие заказы
class OrderProcessor(Order):
    def __init__(self):
        self.orders = {}  # Словарь для хранения заказов
        self.next_order_id = 1  # Начальное значение номера заказа

    def add_order(self, customer, product, quantity):
        order_id = self.next_order_id
        order = Order(customer, product, quantity)
        self.orders[order_id] = order
        self.next_order_id += 1

    def delete_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Заказ {order_id} удален.")
        else:
            print(f"Заказ {order_id} не найден.")
        print("_____")
            
    def update_order(self, order_id, customer_name=None, total_amount=None, product=None):
        # Обновление информации о заказе
        if order_id in self.orders:
            order = self.orders[order_id]
            if customer_name:
                order.customer.name = customer_name
            if total_amount:
                # Assuming total_amount is not a property of Order, modify accordingly
                order.total_amount = total_amount
            if product:
                order.product.name = product
            print(f"Информация по заказу {order_id} обновлена.")
        else:
            print(f"Заказ {order_id} не найден.")
    
    def display_orders(self):
        print("Список заказов:")
        for order_id, order in sorted(self.orders.items()):
            print(f"Заказ {order_id}: {order}")
            
    def display_statistics(self):
        # Вывод статистической информации
        total_orders = len(self.orders)
        total_amount = sum(order.calculate_total_amount() for order in self.orders.values())
        print("_____")
        print(f"Общее количество заказов: {total_orders}")
        print(f"Общая сумма заказов: {total_amount}")
        print("_____")
        
    def display_sorted_orders(self):
        # Вывод отсортированных по номерам заказов
        print("Отсортированный список заказов:")
        for order_id, order in sorted(self.orders.items()):
            print(f"Заказ {order_id}: {order}")
        print("_____")

    def display_sorted_by_amount(self):
        # Вывод отсортированных по сумме заказов
        print("Отсортированный список заказов по сумме:")
        for order_id, order in sorted(self.orders.items(), key=lambda x: x[1].calculate_total_amount()):
            print(f"Заказ {order_id}: {order}")
        print("_____")

def print_menu():
    print("1. Добавить заказ")
    print("2. Обновить заказ")
    print("3. Удалить заказ")
    print("4. Вывести статистику")
    print("5. Вывести список заказов")
    print("6. Вывести отсортированный список заказов")
    print("7. Вывести отсортированный список заказов по сумме")
    print("8. Выход")

if __name__ == "__main__":
    processor = OrderProcessor()
    
    customer1 = Customer("Алексей", "alex@example.com")
    product1 = Product("Монитор", 10000)

    customer2 = Customer("Иван", "ivan@example.com")
    product2 = Product("Моноблок", 1500)

    order_id = processor.next_order_id
            
    # покупатель, товар, кол-во товаров
    processor.add_order(customer1, product1, 1)
    processor.add_order(customer2, product2, 1)

    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            customer_name = input("Введите имя заказчика: ")
            product = input("Введите товар: ")
            total_amount = float(input("Введите сумму заказа: "))
            
            new_customer = Customer(customer_name, "@example.com")
            new_product = Product(product, 1500)
            
            
            processor.add_order(new_customer, new_product, order_id+1)
            
        elif choice == '2':
            order_id = int(input("Введите номер заказа для обновления: "))
            customer_name = input("Введите новое имя заказчика (оставьте пустым, если не хотите изменять): ")
            product = input("Введите новый товар (оставьте пустым, если не хотите изменять): ")
            total_amount = float(input("Введите новую сумму заказа (оставьте пустым, если не хотите изменять): "))
            processor.update_order(order_id, customer_name, total_amount, product)
        elif choice == '3':
            order_id = int(input("Введите номер заказа для удаления: "))
            processor.delete_order(order_id)
        elif choice == '4':
            processor.display_statistics()
        elif choice == '5':
            processor.display_orders()
        elif choice == '6':
            processor.display_sorted_orders()
        elif choice == '7':
            processor.display_sorted_by_amount()
        elif choice == '8':
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите от 1 до 8.")