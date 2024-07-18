"""Завдання 1. Напишіть програму на Python, яка рекурсивно копіює файли у 
вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, 
назви яких базуються на розширенні файлів."""

import os
import shutil
import argparse

def parse_arguments():
    """Парсер аргументів командного рядка."""
    parser = argparse.ArgumentParser(description="Рекурсивно копіює та сортує файли за їх розширеннями.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()

def copy_and_sort_files(src, dst):
    """Копіює файли з вихідної директорії та сортує їх за розширеннями у директорію призначення."""
    # Створює директорію призначення, якщо вона не існує
    if not os.path.exists(dst):
        os.makedirs(dst)

    # Перебирає всі елементи у вихідній директорії
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        if os.path.isdir(src_path):
            # Рекурсивно обробляє піддиректорії
            copy_and_sort_files(src_path, dst)
        else:
            # Отримує розширення файлу без точки
            file_ext = os.path.splitext(item)[1][1:].lower()
            if file_ext:
                # Створює директорію для кожного типу файлу
                ext_dir = os.path.join(dst, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                dst_path = os.path.join(ext_dir, item)
                # Копіює файл, якщо шляхи до файлів не однакові
                if os.path.abspath(src_path) != os.path.abspath(dst_path):
                    shutil.copy2(src_path, dst_path)

def main():
    """Головна функція."""
    args = parse_arguments()
    try:
        copy_and_sort_files(args.source, args.destination)
        print(f"Файли успішно скопійовані та відсортовані у {args.destination}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()
