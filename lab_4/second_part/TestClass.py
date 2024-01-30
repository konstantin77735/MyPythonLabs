class ParentClass:
    def common_method(self):
        print("ParentClass.common_method() called.")


class ChildClass1(ParentClass):
    def specific_method(self):
        print("ChildClass1.specific_method() called.")


class ChildClass2(ParentClass):
    def specific_method(self):
        print("ChildClass2.specific_method() called.")


class ChildClass3(ParentClass):
    def specific_method(self):
        print("ChildClass3.specific_method() called.")


class MyInterface:
    def interface_method(self):
        pass


class ClassImplementingInterface1(MyInterface):
    def interface_method(self):
        print("ClassImplementingInterface1.interface_method() called.")


class ClassImplementingInterface2(MyInterface):
    def interface_method(self):
        print("ClassImplementingInterface2.interface_method() called.")


class ClassImplementingInterface3(MyInterface):
    def interface_method(self):
        print("ClassImplementingInterface3.interface_method() called.")


class TestClass:
    def first_test(self):
        array = [ChildClass1(), ChildClass2()]  # создание массива объектов родительского класса

        # добавление объектов классов-наследников в массив

        # обращение к общим методам этих классов посредством прохода по элементам массива
        for item in array:
            item.common_method()
            print(f"Вызов common_method() у объекта {item.__class__.__name__}")

    def second_test(self):
        array = [ClassImplementingInterface1(), ClassImplementingInterface2()]  # создание массива объектов интерфейса

        # добавление экземпляров классов, реализующих интерфейс

        # вызов методов интерфейса у элементов массива в цикле
        for item in array:
            item.interface_method()
            print(f"Вызов interface_method() у объекта {item.__class__.__name__}")

    @staticmethod
    def main():
        test_class = TestClass()
        choice = -1

        while choice != 0:
            print("Выберите действие:")
            print("1. first_test()")
            print("2. second_test()")
            print("0. Выход")

            choice = int(input())

            if choice == 1:
                test_class.first_test()
            elif choice == 2:
                test_class.second_test()
            elif choice == 0:
                print("Выход из программы.")
            else:
                print("Неверный выбор.")


if __name__ == "__main__":
    TestClass.main()
