from typing import List

from .constants import Descent, Sex
from .generators import NameGenerator


def generate(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX,
    *,
    limit: int
) -> List[str]:
    generator = NameGenerator(descent, sex)
    return generator.generate(limit)


def generate_one(
    descent: Descent = Descent.ENGLISH,
    sex: Sex = Sex.UNISEX
):
    return generate(descent, sex, limit=1)[0]
