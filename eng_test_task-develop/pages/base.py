from playwright.sync_api import Page

__all__ = ["BasePage"]


class BasePage:
    URL = "https://commenter.su"
    page: Page

    def __init__(self, page: Page) -> None:
        self.page = page

    def load(self) -> None:
        self.page.goto(self.URL)
