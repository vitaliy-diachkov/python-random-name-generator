"""Module for storing project constant values & enumerations."""
from enum import Enum


class Descent(Enum):
    """List of available name descents."""

    ENGLISH = 'English'
    ITALIAN = 'Italian'
    FRENCH = 'French'
    GERMAN = 'German'
    RUSSIAN = 'Russian'


class Sex(Enum):
    """List of available name sexes."""

    MALE = 'male'
    FEMALE = 'female'
    UNISEX = 'unisex'


FIRST_NAMES = {
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
"""
First names that are used to generate random names.

This constant follows the next structure:

    {
        DESCENT_VALUE: {
            SEX_VALUE: [
                'first_name_1',
                'first_name_2'
            ]
        }
    }

Leave the first name list blank if there is no male/female/unisex names
set, but don't leave it blank.
"""


LAST_NAMES = {
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
"""
List of last names available to generate random names.

This constant follows the next structure:

    {
        DESCENT_VALUE: [
            'last_name_1',
            'last_name_2'
        ]

        or

        DESCENT_VALUE: {
            SEX_VALUE: [
                'last_name_1',
                'last_name_2'
            ]
        }
    }
"""
