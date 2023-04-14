"""
Regexes!
"""

from typing import Final
import re


_NON_WORDS: Final[str] = r"^\w\s\-\'"


class CharacterSets:
    CONTROL_CHARACTERS_REGEX: Final[re.Pattern] = re.compile('[\x00-\x1F\x7f\x81\x8D\x8F\x90\x9d\xA0\u2028-\u202F\u205F-\u206F\u2400-\u2421]+')


DASH_UNDUPLICATOR_REGEX: Final[re.Pattern] = re.compile(r'\-{2,}')
DASH_AND_SPACE_REGEX: Final[re.Pattern] = re.compile(r'[\s]*-[\s]*')


MATCH_ALL_BRACKETS_AND_CONTENTS_REGEX: Final[re.Pattern] = re.compile(r'\<(.*?)\>|\((.*?)\)|\[(.*?)\]|\{(.*?)\}')
MATCH_CONTENTS_FROM_PARENTHESES_REGEX: Final[re.Pattern] = re.compile(r'\((.*?)\)')
MATCH_DUPLICATED_SPACES_REGEX: Final[re.Pattern] = re.compile(r'[\s]{2,}')
MATCH_LEADING_NON_WORD_CHARACTERS_REGEX: Final[re.Pattern] = re.compile(rf'^[{_NON_WORDS}]*')
MATCH_NON_WORD_CHARACTERS_REGEX: Final[re.Pattern] = re.compile(rf'([{_NON_WORDS}]+)')
MATCH_NUMBERS_REGEX: Final[re.Pattern] = re.compile(r'\d+')
MATCH_TRAILING_NON_WORD_CHARACTERS_REGEX: Final[re.Pattern] = re.compile(rf"[{_NON_WORDS}]$")
MATCH_TRAILING_NON_WORD_CHARACTERS_AND_WHAT_FOLLOW_REGEX: Final[re.Pattern] = re.compile(rf"[{_NON_WORDS}].*$")
MATCH_WORDS_REGEX: Final[re.Pattern] = re.compile(r'(\w+)')


MATCH_TRAILING_NON_LETTERS_EXCEPT_DOT_REGEX: Final[re.Pattern] = re.compile(r'[^\.\w]+$')  #: Remove trailing non-letters except dot, only if they're
                                                                                           #: not followed by any letters / dots.
