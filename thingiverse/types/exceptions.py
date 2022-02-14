
class SearchException(Exception):
    """Used when something went wrong when searching"""
    pass


class ThingiverseException(Exception):
    """Used when a general error happens"""
    pass


class UnathenticatedException(Exception):
    """Used when user is unathenticated"""
    pass


class ResourceNotFound(Exception):
    """Used when a resource like a Thing isn't found"""
    pass


class UserException(Exception):
    """Used when something went wrong when searching"""
    pass
