import pytest

from random_name_generator.constants import Descent, Sex


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
        },
        Descent.FRENCH: {},
        Descent.GERMAN: {
            Sex.MALE: []
        }
    }

    monkeypatch.setattr(
        'random_name_generator.constants.FIRST_NAMES',
        first_names
    )

    return first_names


@pytest.fixture
def mock_last_names(monkeypatch):
    last_names = {
        Descent.ENGLISH: [
            'Abramson',
            'Johnson'
        ],
        Descent.RUSSIAN: {
            Sex.MALE: [
                'Ivanov',
                'Petrov'
            ],
            Sex.FEMALE: [
                'Ivanova',
                'Petrova'
            ]
        }
    }

    monkeypatch.setattr(
        'random_name_generator.constants.LAST_NAMES',
        last_names
    )

    return last_names
