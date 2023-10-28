from enum import unique, IntEnum


@unique
class SubjectType(IntEnum):
    BOOK = 1
    ANIME = 2
    MUSIC = 3
    GAME = 4
    REAL = 6


@unique
class UserGroup(IntEnum):
    ADMIN = 1
    BANGUMI_ADMIN = 2
    DOUJIN_ADMIN = 3
    MUTED_USER = 4
    BLOCKED_USER = 5
    PERSON_ADMIN = 8
    WIKI_ADMIN = 9
    USER = 10
    WIKI_USER = 11


@unique
class BloodType(IntEnum):
    A = 1
    B = 2
    AB = 3
    O = 4


@unique
class CharacterType(IntEnum):
    CHARACTER = 1
    MECHANIC = 2
    SHIP = 3
    ORGANIZATION = 4


@unique
class CollectionType(IntEnum):
    WISH = 1
    DONE = 2
    DOING = 3
    ON_HOLD = 4
    DROPPED = 5


@unique
class EpType(IntEnum):
    MAIN_STORY = 0
    SP = 1
    OP = 2
    ED = 3
    PV = 4
    MAD = 5
    OTHER = 6


@unique
class PersonType(IntEnum):
    INDIVIDUAL = 1
    CORPORATION = 2
    ASSOCIATION = 3


@unique
class SubjectType(IntEnum):
    BOOK = 1
    ANIME = 2
    MUSIC = 3
    GAME = 4
    REAL = 6
