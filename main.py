from logic import summary_file, top_file, errors_file, v_print, v_print1, v_print2
from storage import export_file


# AI log: Були проблеми з непередбачуваним вводом користувача та передачею даних між командами (як зберегти результат команди top для export).
# З допомогою підказок від ментора розібрався, як безпечно розбивати рядок через .split() без аргументів,
# також додав обробку FileNotFoundError для захисту від відсутності файлу.


def main():
    """Програма — Аналізатор Логів"""
    v_print("Програма — Аналізатор Логів")
    v_print2("Щоб дізнатися команди введіть -> help")

    last_result = None

    while True:
        command = input('Введіть вашу команду >>> ')

        try:

            if command == 'help':
                v_print1("Доступні команди: summary, top, export, help, quit.")
                print("Щоб дізнатися детальніше про команду напишіть: help <command>")
                v_print2("Приклади: help summary, help top, help export")

            elif command.startswith('help summary'):
                v_print("Команда <summary> вираховує кількість рядків в файлі.")

            elif command.startswith('help top'):
                v_print1(
                    "Команда <top> показує топ елементів за заданої кількості в конкретній категорії.")
                v_print2("Приклади використання (top <category> <counts>): top ip 5, top status 7, top size 10")

            elif command.startswith('help export'):
                v_print1("Команда <export> зберігає виконання команди в файл.")
                v_print2("Приклади використання (export <filename>): export, export my_log")

            elif command.startswith('help quit'):
                v_print("Команда для завершення роботи програми.")

            elif command == 'summary':
                last_result = summary_file()
                errors, errors_list = errors_file()

                v_print1(f"Кількість рядків в файлі: {last_result}")

                if errors:
                    v_print2(f"Кількість помилок в файлі: {errors}, "
                             f"\nСписок 10 помилок: {errors_list[:10]}")

            elif command.startswith('top'):
                parts = command.split()

                if len(parts) == 1:
                    last_result = top_file()
                    v_print(last_result)

                elif len(parts) == 2:
                    last_result = top_file(w_search=parts[1])
                    v_print(last_result)

                elif len(parts) == 3:
                    try:
                        last_result = top_file(w_search=parts[1], counts=int(parts[2]))
                        v_print(last_result)

                    except ValueError:
                        v_print("Помилка значення 3 аргументу повинно бути числом!")

                else:
                    v_print("Помилка в введенні команди!")

            elif command.startswith('export'):

                if last_result is None:
                    v_print("Ще не було виконано ніяких операцій, зберігати нічого.")

                else:
                    parts = command.split()

                    if len(parts) == 1:
                        export_file(last_result)
                        v_print("Дані успішно експортовано! ")

                    elif len(parts) == 2:

                        if parts[1].endswith('.json'):

                            export_file(last_result, parts[1])
                            v_print(f"Дані успішно експортовано, назва файлу {parts[1]}!")

                        else:
                            export_file(last_result, parts[1] + '.json')
                            v_print(f"Дані успішно експортовано, назва файлу {parts[1]}.json!")

                    else:
                        v_print("Помилка в введенні команди!")

            elif command == 'quit' or command == 'exit':
                v_print1("Виходимо з програми...")
                break

        except FileNotFoundError:
            v_print(f"Помилка файлу не знайдено!")


if __name__ == '__main__':
    main()
