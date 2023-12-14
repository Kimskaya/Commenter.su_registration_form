from pages.base import BasePage

__all__ = ["SignInPage"]


class SignInPage(BasePage):
    def open_modal(self) -> None:
        self.page.click("a[href='#login']")
        self.page.wait_for_selector("#modalForm", timeout=1000.0)

    def fill_email(self, email: str) -> None:
        self.page.fill("#loginEmail", email)

    def fill_password(self, password: str) -> None:
        self.page.fill("#loginPassword", password)

    def press_button(self) -> None:
        self.page.click("#loginBtn")
