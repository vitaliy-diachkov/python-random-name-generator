"""
Random name generators module.

Generators are functions that generates random names.
"""
import random
from typing import List, Union

from .constants import Descent, Sex
from .errors import LimitExceedError
from .selectors import get_first_names, get_last_names


DescentPair = tuple[Descent, Descent]


def generate(
    descent: Union[Descent, DescentPair] = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
    *,
    limit: int,
) -> List[str]:
    """
    Generate random names for given descent and sex in count of limit.

    All names contains unique first names and unique last names. For example,
    you won't get Alex Johnson and Alex Jameson in the same response.

    :param descent: Could be either Descent value or tuple with two Descent
        values. For example, ``Descent.ENGLISH`` or ``(Descent.ENGLISH,
        Descent.ITALIAN)``. When only 1 value is provided, this value would be
        used to generate both first and last name. In case with tuple, the
        first value would be used as a parameter to generate first name,
        the second - to generate last name.
    :param sex: A name sex affiliation.
    :param limit: Number of random names to generate.

    :returns: List of random name pairs (first + last name).
    """
    if isinstance(descent, Descent):
        first_name_descent, last_name_descent = descent, descent
    if isinstance(descent, tuple):
        first_name_descent, last_name_descent = descent

    first_names = get_first_names(first_name_descent, sex)
    last_names = get_last_names(last_name_descent, sex)

    max_random_names = min(len(first_names), len(last_names))

    if max_random_names < limit:
        raise LimitExceedError(descent, sex, max_random_names)

    random.shuffle(first_names)
    random.shuffle(last_names)

    name_pairs = list(zip(first_names, last_names))[:limit]

    return [
        f'{first_name} {last_name}'
        for first_name, last_name
        in name_pairs
    ]


def generate_one(
    descent: Union[Descent, DescentPair] = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
) -> str:
    """
    Generate one random name of given descent and sex.

    :param descent: Could be either Descent value or tuple with two Descent
        values. For example, ``Descent.ENGLISH`` or ``(Descent.ENGLISH,
        Descent.ITALIAN)``. When only 1 value is provided, this value would be
        used to generate both first and last name. In case with tuple, the
        first value would be used as a parameter to generate first name,
        the second - to generate last name.
    :param sex: A name sex affiliation.

    :returns: Random name pair (first + last name).
    """
    names = generate(descent, sex, limit=1)
    return names[0]
