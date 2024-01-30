class OrderProcessor:
    def __init__(self):
        self.orders = {}  # Словарь для хранения заказов
        self.next_order_id = 1  # Начальное значение номера заказа

    def add_order(self, customer_name, total_amount, product):
        # Добавление нового заказа
        order_id = self.next_order_id
        self.orders[order_id] = {'customer_name': customer_name, 'total_amount': float(total_amount), 'product': product}
        self.next_order_id += 1  # Увеличиваем номер для следующего заказа

    def delete_order(self, order_id):
        # Удаление заказа по его идентификатору
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Заказ {order_id} удален.")

            # Обновление номеров заказов после удаления
            updated_orders = {}
            for i, (existing_id, order_info) in enumerate(sorted(self.orders.items())):
                updated_orders[i + 1] = order_info
            self.orders = updated_orders
            self.next_order_id -= 1  # Уменьшаем номер для следующего заказа
        else:
            print(f"Заказ {order_id} не найден.")

    def update_order(self, order_id, customer_name=None, total_amount=None, product=None):
        # Обновление информации о заказе
        if order_id in self.orders:
            if customer_name:
                self.orders[order_id]['customer_name'] = customer_name
            if total_amount:
                self.orders[order_id]['total_amount'] = total_amount
            if product:
                self.orders[order_id]['product'] = product
            print(f"Информация по заказу {order_id} обновлена.")
        else:
            print(f"Заказ {order_id} не найден.")

    def display_orders(self):
        # Вывод всех заказов
        print("Список заказов:")
        for order_id, order_info in sorted(self.orders.items()):
            print(f"Заказ {order_id}: {order_info['customer_name']}, Товар: {order_info['product']}, Сумма: {order_info['total_amount']}")

    def display_statistics(self):
        # Вывод статистической информации
        total_orders = len(self.orders)
        total_amount = sum(order_info['total_amount'] for order_info in self.orders.values())
        print(f"Общее количество заказов: {total_orders}")
        print(f"Общая сумма заказов: {total_amount}")
        print("_____")
        
    def display_sorted_orders(self):
        # Вывод отсортированных по номерам заказов
        print("Отсортированный список заказов:")
        for order_id, order_info in sorted(self.orders.items()):
            print(f"Заказ {order_id}: {order_info['customer_name']}, Товар: {order_info['product']}, Сумма: {order_info['total_amount']}")
        print("_____")

    def display_sorted_by_amount(self):
        # Вывод отсортированных по сумме заказов
        print("Отсортированный список заказов по сумме:")
        for order_id, order_info in sorted(self.orders.items(), key=lambda x: x[1]['total_amount']):
            print(f"Заказ {order_id}: {order_info['customer_name']}, Товар: {order_info['product']}, Сумма: {order_info['total_amount']}")
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
    processor.add_order("Алексей", "100000", "Монитор")
    processor.add_order("Иван", "15000", "Моноблок")

    while True:
        print_menu()
        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            customer_name = input("Введите имя заказчика: ")
            product = input("Введите товар: ")
            total_amount = float(input("Введите сумму заказа: "))
            processor.add_order(customer_name, total_amount, product)
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