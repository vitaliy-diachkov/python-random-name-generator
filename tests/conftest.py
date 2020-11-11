import pytest


pytest_plugins = [
    'tests.fixtures.names'
]


@pytest.fixture
def mock_random_shuffle(monkeypatch):
    def shuffle(*args, **kwargs):
        pass

    monkeypatch.setattr('random.shuffle', shuffle)

    return shuffle
