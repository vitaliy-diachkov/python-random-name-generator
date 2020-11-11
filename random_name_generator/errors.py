"""Custom expection classes module."""
from .constants import Descent, Sex


class NameGenerationError(Exception):
    """Base exception that raised when any generation error has occured."""


class UnsupportedSexError(NameGenerationError):
    """Raises when sex is not supported for given descent."""


class UnsupportedDescentError(NameGenerationError):
    """Raises when given descent is not presented in first/last names list."""


class LimitExceedError(NameGenerationError):
    """Raised when user asked for more random names than it is possible."""

    def __init__(self, descent: Descent, sex: Sex, max_possible_count: int):
        if isinstance(descent, Descent):
            first_name_descent, last_name_descent = descent, descent
        elif isinstance(descent, tuple):
            first_name_descent, last_name_descent = descent

        if first_name_descent == last_name_descent:
            descent_string = first_name_descent.value
        else:
            descent_string = (
                f'{first_name_descent.value}/{last_name_descent.value}'
            )

        self.descent = descent
        self.sex = sex
        self.max_possible_count = max_possible_count

        super().__init__((
            'We can not generate 999 {sex} {descent} names (max. possible '
            'count: {max_count}).'
        ).format(
            sex=sex.value,
            descent=descent_string,
            max_count=max_possible_count
        ))
