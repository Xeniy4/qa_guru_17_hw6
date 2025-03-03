from datetime import time
from pprint import pprint

def test_dark_theme_by_time():
    date_start = time(hour=22)
    date_end = time(hour=6)
    current_time = time(hour=11)
    if  (date_end <= current_time) and (current_time < date_start):
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is False


def test_dark_theme_by_time():
    date_start = time(hour=22)
    date_end = time(hour=6)
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    if date_end < current_time < date_start and dark_theme_enabled_by_user == True:
        is_dark_theme = True
    elif date_end < current_time < date_start and dark_theme_enabled_by_user == False:
        is_dark_theme = False
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time2():
    date_start = time(hour=22)
    date_end = time(hour=6)
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user is None:
        is_dark_theme = not ((date_end <= current_time) and (current_time < date_start))
    else:
        is_dark_theme = dark_theme_enabled_by_user

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for item in users:
        if item["name"] == "Olga":
            suitable_users = item
            # print(item)
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for item in users:
        if item["age"] < 20:
            suitable_users.append(item)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = print_function_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def print_function_and_args(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    arg_names = ', '.join([*args])
    print(f"{func_name} [{arg_names}]")
    return f"{func_name} [{arg_names}]"
