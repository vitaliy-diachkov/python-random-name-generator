import pytest

from random_name_generator import Descent, Sex
from random_name_generator.errors import NameGenerationError
from random_name_generator.selectors import (
    get_first_names,
    get_last_names,
    get_sexes
)


class TestFirstNameSelector:
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


class TestLastNameSelector:
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
