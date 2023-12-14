from pages.base import BasePage

__all__ = ["DashboardPage"]


class DashboardPage(BasePage):
    def login(self, email: str, password: str) -> None:
        self.page.click("a[href='#login']")
        self.page.fill("#loginEmail", email)
        self.page.fill("#loginPassword", password)
        self.page.click("#loginBtn")
