"""Custom expection classes module."""


class NameGenerationError(Exception):
    """Base exception that raised when any generation error has occured."""


class UnsupportedSexError(NameGenerationError):
    """Raises when sex is not supported for given descent."""


class UnsupportedDescentError(NameGenerationError):
    """Raises when given descent is not presented in first/last names list."""


class LimitExceedError(NameGenerationError):
    """Raised when user asked for more random names than it is possible."""
