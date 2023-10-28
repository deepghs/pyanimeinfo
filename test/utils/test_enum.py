from enum import unique, IntEnum

import pytest

from pyanimeinfo.utils import load_from_enum, load_text_from_enum


@unique
class SubjectType(IntEnum):
    BOOK = 1
    ANIME = 2
    MUSIC = 3
    GAME = 4
    REAL = 6


@pytest.mark.unittest
class TestUtilsEnum:
    def test_load_from_enum(self):
        assert load_from_enum(1, SubjectType) is SubjectType.BOOK
        assert load_from_enum(SubjectType.BOOK, SubjectType) is SubjectType.BOOK
        assert load_from_enum('BOOK', SubjectType) is SubjectType.BOOK
        assert load_from_enum('Book', SubjectType) is SubjectType.BOOK

        assert load_from_enum(2, SubjectType) is SubjectType.ANIME
        assert load_from_enum(SubjectType.ANIME, SubjectType) is SubjectType.ANIME
        assert load_from_enum('ANIME', SubjectType) is SubjectType.ANIME
        assert load_from_enum('ANIME  ', SubjectType) is SubjectType.ANIME

        assert load_from_enum(3, SubjectType) is SubjectType.MUSIC
        assert load_from_enum(SubjectType.MUSIC, SubjectType) is SubjectType.MUSIC
        assert load_from_enum('MUSIC', SubjectType) is SubjectType.MUSIC
        assert load_from_enum(' music', SubjectType) is SubjectType.MUSIC

        assert load_from_enum(4, SubjectType) is SubjectType.GAME
        assert load_from_enum(SubjectType.GAME, SubjectType) is SubjectType.GAME
        assert load_from_enum('GAME', SubjectType) is SubjectType.GAME

        assert load_from_enum(6, SubjectType) is SubjectType.REAL
        assert load_from_enum(SubjectType.REAL, SubjectType) is SubjectType.REAL
        assert load_from_enum('REAL', SubjectType) is SubjectType.REAL

        with pytest.raises(TypeError):
            _ = load_from_enum(None, SubjectType)
        with pytest.raises(TypeError):
            _ = load_from_enum([], SubjectType)
        with pytest.raises(ValueError):
            _ = load_from_enum(100, SubjectType)
        with pytest.raises(ValueError):
            _ = load_from_enum('100', SubjectType)

    def test_load_text_from_enum(self):
        assert load_text_from_enum(1, SubjectType) == '1'
        assert load_text_from_enum(SubjectType.BOOK, SubjectType) == '1'
        assert load_text_from_enum('BOOK', SubjectType) == '1'

        assert load_text_from_enum(2, SubjectType) == '2'
        assert load_text_from_enum(SubjectType.ANIME, SubjectType) == '2'
        assert load_text_from_enum('ANIME', SubjectType) == '2'

        assert load_text_from_enum(3, SubjectType) == '3'
        assert load_text_from_enum(SubjectType.MUSIC, SubjectType) == '3'
        assert load_text_from_enum('MUSIC', SubjectType) == '3'

        assert load_text_from_enum(4, SubjectType) == '4'
        assert load_text_from_enum(SubjectType.GAME, SubjectType) == '4'
        assert load_text_from_enum('GAME', SubjectType) == '4'

        assert load_text_from_enum(6, SubjectType) == '6'
        assert load_text_from_enum(SubjectType.REAL, SubjectType) == '6'
        assert load_text_from_enum('REAL', SubjectType) == '6'
