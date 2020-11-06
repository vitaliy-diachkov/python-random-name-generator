import pytest

from random_name_generator.errors import NameGenerationError
from random_name_generator.constants import Descent, Sex
from random_name_generator.utils import (
    get_first_names_list,
    get_sex_list
)


@pytest.fixture
def mock_first_names(monkeypatch):
    first_names = {
        Descent.ENGLISH: {
            Sex.MALE: [
                'John',
                'Joseph'
            ],
            Sex.FEMALE: [
                'Ashley'
            ],
            Sex.UNISEX: [
                'Alex'
            ]
        },
        Descent.ITALIAN: {
            Sex.MALE: [
                'Enzo',
                'Luca'
            ],
            Sex.FEMALE: [
                'Gianna',
            ],
            Sex.UNISEX: [
                'Cosme'
            ]
        }
    }

    monkeypatch.setattr(
        'random_name_generator.constants.FIRST_NAMES',
        first_names
    )

    return first_names


@pytest.mark.parametrize(
    'descent,sex,expected',
    [
        (Descent.ENGLISH, Sex.MALE, ['Alex', 'John', 'Joseph']),
        (Descent.ENGLISH, Sex.FEMALE, ['Alex', 'Ashley']),
        (Descent.ENGLISH, Sex.UNISEX, ['Alex']),
        ('english', 'male', ['Alex', 'John', 'Joseph']),
        ('english', 'female', ['Alex', 'Ashley']),
        ('english', 'unisex', ['Alex'])
    ]
)
def test_get_random_names_list(descent, sex, expected, mock_first_names):
    random_names = get_first_names_list(descent, sex)
    assert random_names == expected


@pytest.mark.parametrize(
    'descent,sex',
    [
        ('french', Sex.UNISEX),
        (Descent.ENGLISH, 'transgender')
    ]
)
def test_get_random_names_list_raises_error(descent, sex, mock_first_names):
    with pytest.raises(NameGenerationError):
        get_first_names_list(descent, sex)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (Sex.MALE, [Sex.MALE, Sex.UNISEX]),
        (Sex.FEMALE, [Sex.FEMALE, Sex.UNISEX]),
        (Sex.UNISEX, [Sex.UNISEX])
    ]
)
def test_get_sex_list(test_input, expected):
    sexes = get_sex_list(test_input)
    assert set(sexes) == set(expected)
