class Program:
    @staticmethod
    def main():
        products_list_1 = ProductList("Магазин №2")
        sales_list_1 = SalesList("Магазин №2")

        sale_1 = Sales("ПК", "Китай", 1000.0, 8000.0, 5, "Перевод по карте", 10000.0, "01.01.2023",
                       "01.01.2024", 1, "Алексеев Святослав", "Техника", 12, 13, 14)

        bathroom_furniture_sale__store_1 = BathroomFurnitureSale("Стул", "Китай", 1000.0, 1500.0, 10, "Перевод по карте",
                                                                 900.0, "01.01.2023", "02.05.2023", 1, "Петров Евгений",
                                                                 "Для ванных комнат", 12, 13, 14)

        kitchen_furniture_sale__store_1 = KitchenFurnitureSale("Стол", "Германия", 100.0, 200.0, 2, "Наличные", 98,
                                                               "01.01.2021", "02.05.2022", 1, "Иванов Сергей", "Для кухни",
                                                               12, 13, 14)

        living_room_furniture_sale__store_1 = LivingRoomFurnitureSale("Шкаф", "Италия", 10, 15, 3, "Оплата по карте", 7,
                                                                       "05.07.2020", "09.09.2020", 1, "Иванов Сергей", "Для гостинной",
                                                                       "Шкаф-купе", 12, 13, 14)

        sales_list_1.add_sales(sale_1)
        sales_list_1.add_sales(bathroom_furniture_sale__store_1)
        sales_list_1.add_sales(kitchen_furniture_sale__store_1)
        sales_list_1.add_sales(living_room_furniture_sale__store_1)

        sales_list_2 = SalesList("Магазин №3")
        kitchen_furniture_sale__store_2 = KitchenFurnitureSale("Стул", "Германия", 200.0, 200.0, 2, "Наличные", 98,
                                                               "01.01.2023", "02.05.2023", 1, "Иванов Сергей", "Для кухни",
                                                               12, 13, 14)

        bathroom_furniture_sale__store_2 = BathroomFurnitureSale("Стул", "Китай", 150.0, 150.0, 10, "Перевод по карте",
                                                                 10.0, "01.01.2022", "02.05.2022", 1, "Иванов Иван",
                                                                 "Для ванных комнат", 12, 13, 14)

        living_room_furniture_sale__store_2 = LivingRoomFurnitureSale("Шкаф", "Италия", 500, 500, 3, "Оплата по карте", 500,
                                                                       "05.07.2021", "09.09.2021", 1, "Иванов Алексей",
                                                                       "Для гостинной", "Шкаф-купе", 12, 13, 14)

        sales_list_2.add_sales(bathroom_furniture_sale__store_2)
        sales_list_2.add_sales(kitchen_furniture_sale__store_2)
        sales_list_2.add_sales(living_room_furniture_sale__store_2)

        products_list_2 = ProductList("Магазин №3")
        sofa = LivingRoomFurnitureProduct("Мягкий диван", "Австралия", 350.0, 375.0, "01.01.2023", "Искусственная кожа",
                                          "Для гостиной", 12, 13, 14)

        table = KitchenFurnitureProduct("Стол обеденный", "Германия", 250.0, 310.0, "01.01.2022", "Дерево", "Для кухни",
                                        12, 13, 14, False)

        mirror = BathroomFurnitureProduct("Зеркало", "Италия", 120.0, 195.0, "01.01.2021", "Стекло", "Для ванной комнаты",
                                          12, 13, 14, False)

        products_list_2.add_products(sofa)
        products_list_2.add_products(table)
        products_list_2.add_products(mirror)

        utilize_list_2 = UtilizeList("Магазин №3")
        utilize_list_2.add_products(table)
        utilize_list_2.add_products(mirror)

        stores = [OnlineStore("Магазин №1", "Пётр Иванов", "2468910562", "www.store_number_1.com"),
                  OnlineStore("Магазин №2", "Александр Петров", "1375911975", "www.store_number_2.com"),
                  OnlineStore("Магазин №3", "Пётр Иванов", "1375911975", "www.store_number_3.com")]

        stores[1].set_products_list_of_store(products_list_1)

        stores[2].set_products_list_of_store(products_list_2)
        stores[2].set_sales_list_of_store(sales_list_2)
        stores[2].set_utilizable_products_list_of_store(utilize_list_2)

        choice = 0

        while choice != -1:
            print("______________________________")
            print("1. Показать магазины")
            print("2. Посмотреть товары в магазине")
            print("3. Посмотреть продажи (проданные товары) в магазине")
            print("4. Посмотреть список утилизируемых товаров в магазине")
            print("5. Посмотреть список покупателей в магазине")
            print("6. Посмотреть список стран-производителей")
            print("0. Выйти из меню")

            choice = int(input("Введите ваш выбор: "))
            
            if choice == 1:
                for store in stores:
                    print(store.name)
            elif choice == 2:
                store_with_products = input("Введите название магазина: ")
                store_with_products_found = False
                for store in stores:
                    if store and store_with_products == store.name:
                        store.print_products("По дате прибытия")
                        store_with_products_found = True
                        break
                if not store_with_products_found:
                    print("Такого магазина не существует.")
            elif choice == 3:
                store_with_sales = input("Введите название магазина: ")
                store_with_sales_found = False
                for store in stores:
                    if store and store_with_sales == store.name:
                        store.print_sales("По дате прибытия")
                        store_with_sales_found = True
                        break
                if not store_with_sales_found:
                    print("Такого магазина не существует.")
            elif choice == 4:
                store_with_utilizable_products = input("Введите название магазина: ")
                store_with_utilizable_products_found = False
                for store in stores:
                    if store and store_with_utilizable_products == store.name:
                        store.print_utilizable_products("По дате прибытия")
                        store_with_utilizable_products_found = True
                        break
                if not store_with_utilizable_products_found:
                    print("Такого магазина не существует.")
            elif choice == 5:
                store_with_customers = input("Введите название магазина: ")
                store_with_customers_found = False
                for store in stores:
                    if store and store_with_customers == store.name:
                        store.print_customers("По дате прибытия")
                        store_with_customers_found = True
                        break
                if not store_with_customers_found:
                    print("Такого магазина не существует.")
            elif choice == 6:
                store_with_countries = input("Введите название магазина: ")
                store_with_countries_found = False
                for store in stores:
                    if store and store_with_countries == store.name:
                        store.print_countries("По дате прибытия")
                        store_with_countries_found = True
                        break
                if not store_with_countries_found:
                    print("Такого магазина не существует.")
            elif choice == 0:
                break
            else:
                print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    Program.main()
