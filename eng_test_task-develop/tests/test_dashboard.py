from playwright.sync_api import Locator

from pages.dashboard import DashboardPage


def test_success(dashboard_page: DashboardPage, email: str, password: str) -> None:
    dashboard_page.load()
    dashboard_page.login(email, password)

    locator: Locator | None = dashboard_page.page.locator("i.myicon-notification")
    assert locator is not None
