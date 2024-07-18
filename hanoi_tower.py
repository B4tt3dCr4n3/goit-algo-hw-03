"""Завдання 3 (необов'язкове завдання). Ханойські башти.
Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, 
використовуючи стрижень В як допоміжний. Диски мають різний розмір і розміщені 
на початковому стрижні у порядку зменшення розміру зверху вниз."""

def hanoi_tower(n, source, auxiliary, target, steps, state):
    """Функція для переміщення дисків з одного стрижня на інший."""
    # Якщо є диски для переміщення
    if n > 0:
        # Переміщуємо n-1 дисків з вихідного стрижня на допоміжний
        hanoi_tower(n-1, source, target, auxiliary, steps, state)
        # Додаємо крок переміщення диска з вихідного стрижня на цільовий
        steps.append(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        # Оновлюємо стан
        state[target].append(state[source].pop())
        steps.append(f"Проміжний стан: {state}")
        # Переміщуємо n-1 дисків з допоміжного стрижня на цільовий
        hanoi_tower(n-1, auxiliary, source, target, steps, state)

def solve_hanoi_tower(n):
    """Функція для розв'язання задачі Ханойські башти."""
    steps = []
    # Початковий стан
    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    steps.append(f"Початковий стан: {state}")
    # Викликаємо рекурсивну функцію для переміщення n дисків
    hanoi_tower(n, 'A', 'B', 'C', steps, state)
    steps.append(f"Кінцевий стан: {state}")
    return steps

if __name__ == "__main__":
    import argparse
    # Створюємо парсер аргументів командного рядка
    parser = argparse.ArgumentParser(description="Розв'язання задачі Ханойські башти.")
    parser.add_argument("n", type=int, help="Кількість дисків")
    args = parser.parse_args()

    # Отримуємо кроки переміщення дисків
    steps = solve_hanoi_tower(args.n)
    # Виводимо кожен крок на екран
    for step in steps:
        print(step)
