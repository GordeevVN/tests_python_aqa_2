import pytest
@pytest.fixture
def browser(scoope="session"):
    print("Браузер")
    pass
    yield
    print("Закрываем браузер")