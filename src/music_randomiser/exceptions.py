class MusicRandomiserError(Exception):
    """Base Exception for all music_randomiser errors"""

    pass


class DatabaseError(MusicRandomiserError):
    """Raised when underlying database operations fail"""

    pass


class ReadXmlError(MusicRandomiserError):
    """Raised when underlying database operations fail"""

    pass
