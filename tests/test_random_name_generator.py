import pytest

from random_name_generator import (
    get_first_names,
    get_last_names,
    get_sexes,
    generate_one,
    generate,
    pick_random_name,
    Descent,
    Sex
)
from random_name_generator.errors import NameGenerationError


@pytest.fixture
def mock_random_picker(monkeypatch):
    def random_picker_mock(initial):
        return initial[0]

    monkeypatch.setattr(
        'random_name_generator.utils.pick_random_name',
        random_picker_mock
    )

    return random_picker_mock


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


class TestFirstNameGenerator:
    @pytest.mark.parametrize(
        'descent,sex,expected',
        [
            (Descent.ENGLISH, Sex.MALE, ['Alex', 'John', 'Joseph']),
            (Descent.ENGLISH, Sex.FEMALE, ['Alex', 'Ashley']),
            (Descent.ENGLISH, Sex.UNISEX, ['Alex']),
        ]
    )
    def test_get_first_names(self, descent, sex, expected, mock_first_names):
        first_names = get_first_names(descent, sex)
        assert first_names == expected

    @pytest.mark.parametrize(
        'descent,sex',
        [
            (Descent.GERMAN, Sex.MALE),
            (Descent.FRENCH, Sex.MALE)
        ]
    )
    def test_first_names_generating_errors(
            self,
            descent,
            sex,
            mock_first_names
    ):
        with pytest.raises(NameGenerationError):
            get_first_names(descent, Sex)


class TestLastNameGenerator:
    @pytest.mark.parametrize(
        'descent,sex,expected',
        [
            (Descent.ENGLISH, Sex.UNISEX, ['Abramson', 'Johnson']),
            (Descent.RUSSIAN, Sex.MALE, ['Ivanov', 'Petrov']),
            (Descent.RUSSIAN, Sex.FEMALE, ['Ivanova', 'Petrova']),
        ]
    )
    def test_get_last_names(self, descent, sex, expected, mock_last_names):
        last_names = get_last_names(descent, sex)
        assert last_names == expected

    def test_get_last_names_unsopported_sex(self, mock_last_names):
        with pytest.raises(NameGenerationError):
            get_last_names(Descent.RUSSIAN)


class TestRandomNamePicker:
    def test_pick_random_name_simple(self):
        names = ['John']
        random_name = pick_random_name(names)
        assert random_name == 'John'

    def test_pick_random_name_conteins(self, mock_first_names):
        first_names = get_first_names(Descent.ENGLISH)
        random_name = pick_random_name(first_names)
        assert random_name in first_names


class TestFullNameGenerator:
    def test_generate_name(
        self,
        mock_first_names,
        mock_last_names,
        mock_random_picker
    ):
        name = generate_one(Descent.ENGLISH, Sex.MALE)
        assert name == 'Alex Abramson'

    def test_generate_names_limit(self, mock_first_names, mock_last_names):
        names = generate(Descent.ENGLISH, Sex.MALE, limit=2)
        assert len(names) == 2

    def test_generate_names_no_duplicates(mock_first_names, mock_last_names):
        names = generate(Descent.ENGLISH, Sex.MALE, limit=6)
        assert not any(names.count(name) > 1 for name in names)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (Sex.MALE, [Sex.MALE, Sex.UNISEX]),
        (Sex.FEMALE, [Sex.FEMALE, Sex.UNISEX]),
        (Sex.UNISEX, [Sex.UNISEX])
    ]
)
def test_get_sex_list(test_input, expected):
    sexes = get_sexes(test_input)
    assert set(sexes) == set(expected)
