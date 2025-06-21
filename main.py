"""
Главный модуль консольного калькулятора.
"""

from operations import add, subtract, multiply, divide
from utils import HistoryManager


def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число!")


def get_operation():

    operations = {"+": "сложение", "-": "вычитание", "*": "умножение", "/": "деление"}

    print("\nДоступные операции:")
    for op, name in operations.items():
        print(f"  {op} - {name}")

    while True:
        operation = input("Выберите операцию (+, -, *, /): ").strip()
        if operation in operations:
            return operation
        print("Ошибка: Выберите корректную операцию!")


def calculate(num1, num2, operation):

    try:
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        expression = f"{num1} {operation} {num2}"
        return result, expression

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")
        return None, None


def show_menu():
    """Показывает главное меню."""
    print("\n" + "=" * 50)
    print("           КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР")
    print("=" * 50)
    print("1. Выполнить вычисление")
    print("2. Показать историю")
    print("3. Очистить историю")
    print("4. Выход")
    print("=" * 50)


def main():
    """Главная функция программы."""
    print("Добро пожаловать в консольный калькулятор!")

    # Создаем менеджер истории
    history_manager = HistoryManager()

    while True:
        show_menu()

        try:
            choice = input("Выберите действие (1-4): ").strip()

            if choice == "1":
                # Выполнение вычисления
                print("\n--- ВЫЧИСЛЕНИЕ ---")
                num1 = get_number("Введите первое число: ")
                operation = get_operation()
                num2 = get_number("Введите второе число: ")

                result, expression = calculate(num1, num2, operation)

                if result is not None:
                    print(f"\nРезультат: {expression} = {result}")
                    history_manager.add_entry(expression, result)

            elif choice == "2":
                # Показать историю
                history_manager.show_history()

            elif choice == "3":
                # Очистить историю
                confirm = input("Вы уверены, что хотите очистить историю? (y/n): ")
                if confirm.lower() in ["y", "yes", "да", "д"]:
                    history_manager.clear_history()

            elif choice == "4":
                # Выход
                print("Спасибо за использование калькулятора!")
                break

            else:
                print("Ошибка: Выберите число от 1 до 4!")

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break
        except Exception as e:
            print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
