import os
import sys
import platform


# Переменные
system_name = platform.system()
system_version = platform.version()
machine = platform.machine()
processor = platform.processor()

# Список для хранения результатов
results = [
    system_name,
    system_version,
    machine,
    processor
]


def show_system_info():
    """Выводит информацию об операционной системе."""
    sys.stdout.write("\n--- Информация о системе ---\n")
    sys.stdout.write(f"Операционная система: {results[0]}\n")
    sys.stdout.write(f"Версия ОС: {results[1]}\n")
    sys.stdout.write(f"Архитектура: {results[2]}\n")
    sys.stdout.write(f"Процессор: {results[3]}\n")


def show_current_directory():
    """Выводит текущую рабочую директорию."""
    current_directory = os.getcwd()
    results.append(current_directory)

    sys.stdout.write("\n--- Текущая директория ---\n")
    sys.stdout.write(f"{current_directory}\n")


def show_python_info():
    """Выводит информацию о Python."""
    python_version = sys.version
    python_executable = sys.executable

    results.append(python_version)
    results.append(python_executable)

    sys.stdout.write("\n--- Информация о Python ---\n")
    sys.stdout.write(f"Версия Python: {python_version}\n")
    sys.stdout.write(f"Интерпретатор: {python_executable}\n")


def show_environment():
    """Выводит информацию об окружении."""
    username = os.environ.get("USERNAME", "Неизвестно")
    computer_name = os.environ.get("COMPUTERNAME", "Неизвестно")

    results.append(username)
    results.append(computer_name)

    sys.stdout.write("\n--- Окружение ---\n")
    sys.stdout.write(f"Пользователь: {username}\n")
    sys.stdout.write(f"Имя компьютера: {computer_name}\n")


def show_saved_results():
    """Выводит все сохранённые результаты."""
    sys.stdout.write("\n--- Сохранённые результаты ---\n")

    for index, result in enumerate(results):
        sys.stdout.write(f"[{index}] {result}\n")


def main():
    while True:
        sys.stdout.write("\n")
        sys.stdout.write("========== ДИАГНОСТИКА СИСТЕМЫ ==========\n")
        sys.stdout.write("1. Информация об операционной системе\n")
        sys.stdout.write("2. Текущая директория\n")
        sys.stdout.write("3. Информация о Python\n")
        sys.stdout.write("4. Информация об окружении\n")
        sys.stdout.write("5. Показать сохранённые результаты\n")
        sys.stdout.write("0. Выход\n")
        sys.stdout.write("Выберите пункт: ")

        choice = sys.stdin.readline().strip()

        if choice == "1":
            show_system_info()

        elif choice == "2":
            show_current_directory()

        elif choice == "3":
            show_python_info()

        elif choice == "4":
            show_environment()

        elif choice == "5":
            show_saved_results()

        elif choice == "0":
            sys.stdout.write("Программа завершена.\n")
            break

        else:
            sys.stdout.write("Ошибка: такого пункта меню нет.\n")


if __name__ == "__main__":
    main()