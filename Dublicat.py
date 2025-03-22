import os
import pyfiglet
from colorama import Fore, init

# Инициализация colorama
init(autoreset=True)

def print_banner():
    """Выводит ASCII-арт заголовок."""
    ascii_art = pyfiglet.figlet_format("DUBLICATOR Fast")
    by_text = "By https://t.me/sukhanovhennadii"
    print(f"\n{Fore.YELLOW}{ascii_art}{by_text.center(80)}\n")

def read_unique_lines(file_path="data.txt"):
    """Читает файл и возвращает уникальные строки."""
    if not os.path.exists(file_path):
        print("Файл не найден!")
        return set()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = set(line.strip() for line in file if line.strip())
    return lines

def create_duplicates(lines, duplicates, output_file):
    """Создает файл с нужным количеством дубликатов."""
    if not output_file.endswith(".txt"):
        output_file += ".txt"
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            for _ in range(duplicates):
                file.write(line + '\n')
    print(f"Файл '{output_file}' создан с {duplicates} дубликатами на каждую строку.")

def main():
    print_banner()
    unique_lines = read_unique_lines()
    
    if not unique_lines:
        print("Нет уникальных строк для обработки.")
        return
    
    try:
        duplicates = int(input("Введите количество дубликатов для каждой строки: "))
        if duplicates < 1:
            print("Число дубликатов должно быть минимум 1.")
            return
    except ValueError:
        print("Введите корректное число.")
        return
    
    output_file = input("Введите имя выходного файла: ").strip()
    create_duplicates(unique_lines, duplicates, output_file)

if __name__ == "__main__":
    main()
