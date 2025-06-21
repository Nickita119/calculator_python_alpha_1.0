from datetime import datetime
import os


class HistoryManager:
    def __init__(self, filename="calculator_history.txt"):
        self.filename = filename
        self.history = []

    def add_entry(self, expression, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {expression} = {result}"
        self.history.append(entry)

    # Сохраняем в файл
    def _save_to_file(self, entry):
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(entry + "\n")
        except Exception as error:
            print(f"Ошибка при сохранении в файл: {e}")

    def show_history(self, lines=10):
        if not self.history:
            print("История пуста. ")
            return

        print(f"\nПоследние {min(lines, len(self.history))} записей: ")
        print("-" * 50)
        for entry in self.history[-lines]:
            print(entry)
        print("-" * 50)

    def clear_history(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write("")
            print("История очищена.")
        except Exception as error:
            print(f"Ошибка при очистке истории: {error}")
