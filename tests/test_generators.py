import pytest

from random_name_generator import generate, generate_one, Descent, Sex
from random_name_generator.errors import LimitExceedError


@pytest.fixture
def mock_random_shuffle(monkeypatch):
    def shuffle(*args, **kwargs):
        pass

    monkeypatch.setattr('random.shuffle', shuffle)

    return shuffle


@pytest.mark.usefixtures(
    'mock_random_shuffle',
    'mock_first_names',
    'mock_last_names'
)
class TestRandomNameGeneration:
    def test_generate_one(self):
        name = generate_one(Descent.ENGLISH, Sex.MALE)
        return name == 'Alex Abramson'

    def test_generate_limit(self):
        names = generate(sex=Sex.MALE, limit=2)
        assert len(names) == 2

    def test_generate_names_no_duplicates(self):
        names = generate(Descent.ENGLISH, Sex.MALE, limit=2)
        assert not any(names.count(name) > 1 for name in names)

    def test_generate_names_too_big_limit(self):
        with pytest.raises(LimitExceedError):
            generate(Descent.ENGLISH, Sex.MALE, limit=999)

    def test_generate_name_with_different_descents(self):
        name = generate_one(
            (Descent.ENGLISH, Descent.ITALIAN),
            sex=Sex.MALE
        )
        assert name == 'Alex Gotti'
