# AI log: самостійно написав логіку читання логу, а з допомогою ментора перейшов до ітерації через генератор (yield) для економії пам'яті,
# зробив збір пошкоджених рядків та налаштував повернення кількості і самого списку помилок через кортеж.

import json


def open_file(filename='access.log'):
    with open(filename, encoding='utf-8') as file:
        error_string = 0
        error_list = []

        for f_string in file:
            f_strip = f_string.split()

            if len(f_strip) == 6:
                timestamp, ip, method, path, status, size = f_strip

                yield {'timestamp': timestamp,
                       'ip': ip,
                       'method': method,
                       'path': path,
                       'status': status,
                       'size': size,
                       }
            else:
                error_string += 1
                error_list.append(f_string.strip('\n'))

        yield error_string, error_list


def export_file(last_result, filename="file.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(last_result, file, ensure_ascii=False, indent=4)
