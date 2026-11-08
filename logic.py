# AI log: самостійно написав базову логіку, після чого з підказками від ментора оптимізував цикли (прибрав enumerate). За його порадою застосував метод .get() з
# перевіркою на None для захисту від KeyError при введенні неіснуючих категорій, а також налаштував розпакування кортежу для функції errors_file.

from storage import open_file


def summary_file(file_name='access.log'):
    summary = 0

    for dicts in open_file(file_name):
        if type(dicts) is dict:
            summary += 1

    return summary


def top_file(file_name='access.log', w_search='ip', counts=5):
    ip_counts = {}

    for dicts in open_file(file_name):

        if type(dicts) is dict:
            w_search_ = dicts.get(w_search, None)

            if w_search_ is not None:
                ip_counts[w_search_] = ip_counts.get(w_search_, 0) + 1

    return [ip_list[0] for ip_list in sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)[:counts]]


def errors_file(file_name='access.log'):
    for dicts in open_file(file_name):

        if type(dicts) is tuple:
            errors, errors_list = dicts

    return errors, errors_list


t = '-' * 50


def v_print(func):
    print(t)
    print(func)
    print(t)


def v_print1(func):
    print(t)
    print(func)


def v_print2(func):
    print(func)
    print(t)
