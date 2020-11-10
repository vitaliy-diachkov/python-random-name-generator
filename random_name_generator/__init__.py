"""
Python Random Name Generator or simply RNG.

This library provides API to generate N random names of different descents.

Usage:

    >>> import random_name_generator as rng
    >>> rng.generate(rng.Descent.ENGLISH, rng.Sex.UNISEX, limit=2)

    or

    >>> rng.generate_one()

    or

    >>> rng.generate(
    ...     descent=(rng.Descent.English, rng.Descent.ITALIAN),
    ...     sex=rng.Sex.UNISEX,
    ...     limit=2)
"""
from .constants import Descent, Sex  # noqa
from .generators import generate, generate_one  # noqa
