from pages.base import BasePage

__all__ = ["SignUpPage"]


class SignUpPage(BasePage):
    def open_modal(self) -> None:
        self.page.click("a[href='#registration']")
        self.page.wait_for_selector("#modalForm", timeout=1000.0)

    def fill_email(self, email: str) -> None:
        self.page.fill("#registerEmail", email)

    def fill_password(self, password: str) -> None:
        self.page.fill("#registerPassword", password)

    def press_button(self) -> None:
        self.page.click("#registerBtn")
