"""Завдання 2. Напишіть програму на Python, яка використовує рекурсію для 
створення фракталу «сніжинка Коха» за умови, що користувач повинен мати можливість 
вказати рівень рекурсії."""

import turtle
import argparse

def koch_snowflake(length, depth):
    """Функція для малювання сніжинки Коха."""
    # Базовий випадок
    if depth == 0:
        turtle.forward(length) # Малює відрізок довжиною length
        return
    length /= 3.0 # Розраховує довжину сторони
    koch_snowflake(length, depth-1) # Рекурсивний виклик
    turtle.left(60) # Поворот на 60 градусів
    koch_snowflake(length, depth-1) # Рекурсивний виклик
    turtle.right(120) # Поворот на 120 градусів
    koch_snowflake(length, depth-1) # Рекурсивний виклик
    turtle.left(60) # Поворот на 60 градусів
    koch_snowflake(length, depth-1) # Рекурсивний виклик

def draw_koch_snowflake(length, depth):
    """Функція для малювання сніжинки Коха."""
    turtle.speed(0) # Найвища швидкість
    turtle.penup() # Піднімає перо
    turtle.goto(-length/2, length/3) # Переміщує відрізок в центр екрану
    turtle.pendown() # Опускає перо
    for _ in range(3): # Малює три сторони сніжинки
        koch_snowflake(length, depth) # Викликає функцію
        turtle.right(120) # Поворот на 120 градусів
    turtle.hideturtle() # Ховає відображення пера
    turtle.done() # Завершує роботу з turtle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Малює сніжинку Коха.") # Створює парсер аргументів
    parser.add_argument("length", type=int, help="Довжина однієї сторони сніжинки") # Додає аргумент довжини
    parser.add_argument("depth", type=int, help="Глибина рекурсії") # Додає аргумент глибини
    args = parser.parse_args() # Парсить аргументи

    draw_koch_snowflake(args.length, args.depth) # Викликає функцію малювання
