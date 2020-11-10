"""
Name selectors module.

Selectors are functions that selects appropriate list of names (first/last
names) for certain sex and descent.
"""
from itertools import chain
from typing import List, Optional

from .errors import UnsupportedDescentError, UnsupportedSexError
from .constants import Descent, Sex, FIRST_NAMES, LAST_NAMES


def get_first_names(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
) -> List[str]:
    """
    Get list of first names of given descent and matching given sex.

    :param descent: Ethnic origin of first name.
    :param sex: Sex affiliation of first name.

    :returns: List of first names.
    """
    names_by_descent = FIRST_NAMES.get(descent)

    if not names_by_descent:
        raise UnsupportedDescentError(
            f'We do not support {descent} descent at this moment'
        )

    sexes = get_sexes(sex)
    random_first_names = sorted(chain.from_iterable(
        names_by_descent.get(sex, [])
        for sex in sexes
    ))

    if not random_first_names:
        raise UnsupportedSexError(
            f'We can not generate {sex} {descent} names at this moment'
        )

    return random_first_names


def get_last_names(
    descent: Descent = Descent.ENGLISH,
    sex: Optional[Sex] = None
) -> List[str]:
    """
    Get list of last names of given descent and matching given sex.

    :param descent: Ethnic origin of last name.
    :param sex: Sex affiliation of last name.

    :returns: List of first names.
    """
    last_names = LAST_NAMES.get(descent)

    if isinstance(last_names, dict):
        if sex is None:
            raise UnsupportedSexError(
                'You need to explicitly set sex to get list of last names for '
                f'{descent} descent'
            )

        if sex not in [Sex.MALE, Sex.FEMALE]:
            raise UnsupportedSexError(
                f'{sex} is not supported for {descent} descent.'
            )

        last_names = last_names.get(sex)

    if not last_names:
        raise UnsupportedDescentError(
            f'We can not get {sex} {descent} last names.'
        )

    return last_names


def get_sexes(initial: Sex) -> List[Sex]:
    """
    Determines name sex affiliation that can match given sex.

    For example, unisex names can also match male and female requests, so they
    should be included into response.
    """
    if initial in [Sex.MALE, Sex.FEMALE]:
        return [initial, Sex.UNISEX]
    if initial is Sex.UNISEX:
        return [Sex.UNISEX]
