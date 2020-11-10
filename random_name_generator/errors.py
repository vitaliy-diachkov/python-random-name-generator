class NameGenerationError(Exception):
    """Raised when we are not able to generate names."""


class UnsupportedSexError(NameGenerationError):
    pass


class UnsupportedDescentError(NameGenerationError):
    pass


class LimitExceedError(NameGenerationError):
    pass
