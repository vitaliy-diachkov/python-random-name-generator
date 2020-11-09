from enum import Enum


class Descent(Enum):
    ENGLISH = 'English'
    ITALIAN = 'Italian'
    FRENCH = 'French'
    GERMAN = 'German'
    RUSSIAN = 'Russian'


class Sex(Enum):
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
