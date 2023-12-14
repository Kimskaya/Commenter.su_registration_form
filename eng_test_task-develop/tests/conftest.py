import os
import secrets
import string

import pytest
from playwright.sync_api import Page

from pages.dashboard import DashboardPage
from pages.sign_in import SignInPage
from pages.sign_up import SignUpPage


@pytest.fixture
def sign_up_page(page: Page) -> SignUpPage:
    return SignUpPage(page)


@pytest.fixture
def sign_in_page(page: Page) -> SignInPage:
    return SignInPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def rand_string() -> str:
    return "".join(secrets.choice(string.ascii_letters + string.digits) for i in range(8))


@pytest.fixture
def email() -> str:
    return os.getenv("SIGN_IN_EMAIL")


@pytest.fixture
def password() -> str:
    return os.getenv("SIGN_IN_PASSWORD")
