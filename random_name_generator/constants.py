from enum import Enum


class Descent(Enum):
    ENGLISH = 'english'
    ITALIAN = 'italian'


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
