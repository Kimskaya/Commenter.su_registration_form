from playwright.sync_api import Locator, expect

from pages.sign_in import SignInPage

MESSAGES = {
    "succeed": "Тарифы",
    "empty_field": "Не указан логин или пароль",
}


def test_success(sign_in_page: SignInPage, email: str, password: str) -> None:
    sign_in_page.load()
    sign_in_page.open_modal()
    sign_in_page.fill_email(email)
    sign_in_page.fill_password(password)

    sign_in_page.press_button()

    locator: Locator | None = sign_in_page.page.locator("i.myicon-notification")
    assert locator is not None


def test_empty_email(sign_in_page: SignInPage, password: str) -> None:
    sign_in_page.load()
    sign_in_page.open_modal()
    sign_in_page.fill_password(password)

    sign_in_page.press_button()

    locator: Locator | None = sign_in_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_empty_password(sign_in_page: SignInPage, email: str) -> None:
    sign_in_page.load()
    sign_in_page.open_modal()
    sign_in_page.fill_email(email)

    sign_in_page.press_button()

    locator: Locator | None = sign_in_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_empty_email_and_password(sign_in_page: SignInPage) -> None:
    sign_in_page.load()
    sign_in_page.open_modal()

    sign_in_page.press_button()

    locator: Locator | None = sign_in_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])


def test_wrong_email(sign_in_page: SignInPage, password: str) -> None:
    sign_in_page.load()
    sign_in_page.open_modal()
    sign_in_page.fill_email("()**^&%$")
    sign_in_page.fill_password(password)

    sign_in_page.press_button()

    locator: Locator | None = sign_in_page.page.locator(".materialert-text")
    assert locator is not None
    expect(locator).to_contain_text(MESSAGES["empty_field"])
