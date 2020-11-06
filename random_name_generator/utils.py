from itertools import chain
from typing import List, Union

from .errors import NameGenerationError
from .constants import Descent, Sex, FIRST_NAMES


def get_first_names_list(
    descent: Union[Descent, str] = Descent.ENGLISH,
    sex: Union[Sex, str] = Sex.UNISEX
) -> List[str]:
    if isinstance(descent, str):
        try:
            descent = Descent(descent)
        except ValueError:
            raise NameGenerationError(f'No descent named {descent}')

    if isinstance(sex, str):
        try:
            sex = Sex(sex)
        except ValueError:
            raise NameGenerationError(f'No sex named {sex}')

    names_by_descent = FIRST_NAMES.get(descent)
    sexes = get_sex_list(sex)
    return sorted(chain.from_iterable(
        names_by_descent.get(sex, [])
        for sex in sexes
    ))


def get_sex_list(initial: Sex) -> List[Sex]:
    if initial in [Sex.MALE, Sex.FEMALE]:
        return [initial, Sex.UNISEX]
    if initial is Sex.UNISEX:
        return [Sex.UNISEX]
