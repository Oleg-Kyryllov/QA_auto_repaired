from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page_NP import SignInPageNP
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_check_NovaPoshta_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPageNP()

    # відкриваємо сторінку https://my.novaposhta.ua/auth
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to NOVAPOSHTA · NOVAPOSHTA")

    # Закриваємо браузер
    sign_in_page.close()
