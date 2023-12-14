from playwright.sync_api import Locator, expect

from pages.sign_up import SignUpPage

MESSAGES = {
    "succeed": "На почту придет письмо для активации аккаунта",
    "empty_field": "Не указан Email или пароль",
}


def test_success(sign_up_page: SignUpPage, rand_string: str) -> None:
    sign_up_page.load()
    sign_up_page.open_modal()
    sign_up_page.fill_email(f"{rand_string}@gmail.com")
    sign_up_page.fill_password(rand_string)

    sign_up_page.press_button()

    locator: Locator | None = sign_up_page.page.locator(".modal-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["succeed"])


def test_empty_email(sign_up_page: SignUpPage, rand_string: str) -> None:
    sign_up_page.load()
    sign_up_page.open_modal()
    sign_up_page.fill_password(rand_string)

    sign_up_page.press_button()

    locator: Locator | None = sign_up_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_empty_password(sign_up_page: SignUpPage, rand_string: str) -> None:
    sign_up_page.load()
    sign_up_page.open_modal()
    sign_up_page.fill_email(f"{rand_string}@gmail.com")

    sign_up_page.press_button()

    locator: Locator | None = sign_up_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_empty_email_and_password(sign_up_page: SignUpPage, rand_string: str) -> None:
    sign_up_page.load()
    sign_up_page.open_modal()

    sign_up_page.press_button()

    locator: Locator | None = sign_up_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_wrong_email(sign_up_page: SignUpPage, rand_string: str) -> None:
    sign_up_page.load()
    sign_up_page.open_modal()
    sign_up_page.fill_email(rand_string)
    sign_up_page.fill_password(rand_string)

    sign_up_page.press_button()

    locator: Locator | None = sign_up_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])
