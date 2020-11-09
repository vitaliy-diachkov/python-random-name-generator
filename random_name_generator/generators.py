from typing import List

from . import utils
from .errors import NameGenerationError
from .constants import Descent, Sex


class NameGenerator:
    def __init__(self, descent: Descent, sex: Sex):
        self._descent = descent
        self._sex = sex

    def generate(self, limit: int) -> List[str]:
        first_names = utils.get_first_names(self._descent, self._sex)
        last_names = utils.get_last_names(self._descent, self._sex)

        possible_combinations = len(first_names) * len(last_names)

        if possible_combinations < limit:
            raise NameGenerationError(
                f'We can not generate more then {possible_combinations} '
                f'{self._sex} names for {self._descent} descent'
            )

        result = []

        for _ in range(limit):
            name = self._generate_one(first_names, last_names)

            while name in result:
                name = self._generate_one(first_names, last_names)

            result.append(name)
        return result

    def _generate_one(
        self,
        first_names: List[str],
        last_names: List[str]
    ) -> str:
        first_name = utils.pick_random_name(first_names)
        last_name = utils.pick_random_name(last_names)
        return f'{first_name} {last_name}'
