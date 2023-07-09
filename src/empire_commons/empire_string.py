from __future__ import annotations

import os
import random
import re
import string
from typing import Sequence, Any, Final

from empire_commons import string_casing
from empire_commons.regex_util import RegexUtil
from empire_commons.reference_data.unicode_transliteration import standard_transliterate
from empire_commons.regexes import MATCH_CONTENTS_FROM_PARENTHESES_REGEX, MATCH_WORDS_REGEX, MATCH_NON_WORD_CHARACTERS_REGEX, \
    MATCH_ALL_BRACKETS_AND_CONTENTS_REGEX, MATCH_LEADING_NON_WORD_CHARACTERS_REGEX, MATCH_TRAILING_NON_WORD_CHARACTERS_REGEX


class String(str):
    NL: Final[str] = '\n'
    TAB: Final[str] = '\t'

    # ======================================================================================== STATIC BUILDERS
    @staticmethod
    def build_empire_strings_from_sequence_strip_nones(sequence: Sequence[Any]) -> list[String]:
        return list(map(lambda x: String(x), filter(None, sequence)))

    @staticmethod
    def generate_random_string(string_length: int, *, lowercase: bool = False) -> String:
        """
        Generates a random string of length *string_length*.
        """
        random_string: str = "".join(
            random.choice(string.ascii_uppercase) for _ in range(string_length)
        )

        return String(random_string.lower() if lowercase else random_string)

    @staticmethod
    def times(string: str | 'String', amount: int) -> String:
        """
        Returns *string* * *amount*.

        If *amount* < 0, amount will be set to 0
        """
        if amount < 0:
            amount = 0

        return String(string * amount)

    @staticmethod
    def quote(string: str | 'String') -> String:
        if "'" not in string:
            return String(f"'{string}'")
        elif '"' not in string:
            return String(f'"{string}"')
        elif "'''" not in string:
            return String(f"'''{string}'''")
        elif '"""' not in string:
            return String(f'"""{string}"""')
        else:
            string = string.replace("'", "\\'").replace('"', '\\"')
            return String(string)

    # =========================================================================================== CONTAINS
    def contains_any_of(self, *what: str | 'String', case_sensitive: bool = True) -> bool:
        """
        Returns True if *the_string* contains any of *what*.
        """
        # doc-src: https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
        if not case_sensitive:
            string: str = self.lower()
        else:
            string: str = self

        return any(item in string for item in what)

    # ============================================================================================ EXTRACTION
    def extract_content_from_parentheses(self) -> tuple[String, ...]:
        """
        Extracts content from parentheses found in string *s*. The result is a tuple of strings, each one without the surrounding parentheses.
        """
        return tuple(
            String.build_empire_strings_from_sequence_strip_nones(MATCH_CONTENTS_FROM_PARENTHESES_REGEX.findall(self))
        )

    def extract_words(self) -> tuple[str, ...]:
        """
        Extracts every word from *s*. The difference between this method and :func:`str.split()`
        is that this method will split with any punctuation, and non-word characters. The extracted
        words also are stripped of these characters described at the end of the last sentence.
        """
        return tuple(
            String.build_empire_strings_from_sequence_strip_nones(MATCH_WORDS_REGEX.findall(self))
        )

    # ============================================================================================ JOINING
    @staticmethod
    def join_non_nulls_non_empty(
        strings: list[str | 'String'], separator: str | 'String'
    ) -> String:  # TODO: improve
        result: str = ""
        for s in strings:
            if s:
                result += s + separator

        return String(result[0 : -len(separator)])

    # ========================================================================================== REPLACEMENT
    def rreplace(self, replacee: str | 'String', replacement: str | 'String' = '', count: int = 1) -> String:
        """
        Replaces starting from the right of string.
        """
        # src: https://stackoverflow.com/questions/9943504/right-to-left-string-replace-in-python
        return String(replacement.join(self.rsplit(replacee, count)))

    def replace_all(self, *replacees: str | 'String', replacement: str | 'String' = "") -> String:
        """
        Replaces all occurrences of *replacees* to *replacement* in *input_string*
        """
        string: str = self
        for replacee in replacees:
            string: str = string.replace(replacee, replacement)

        return String(string)

    def replace_all_except_alpha_numerical_characters(self, *, with_: str | 'String' = '') -> String:
        """
        Replace all non-alpha numerical characters with the specified replacement string.
        """
        return String(MATCH_NON_WORD_CHARACTERS_REGEX.sub(with_, self))

    def replace_brackets_and_content(
        self, *, with_: str | 'String' = ''
    ) -> String:
        """
        Replaces (), [], {}, <> and whatever they contain with the specified replacement string.
        """
        return String(MATCH_ALL_BRACKETS_AND_CONTENTS_REGEX.sub(
            with_, self
        ))

    def replace_characters(self, *characters_to_replace: str | 'String', with_: str | 'String' = '') -> String:
        """
        Replace all specified characters with the specified replacement string.
        """
        regex = RegexUtil.get_compiled_re_with_joined_tokens('{}', '|', *characters_to_replace)
        return String(regex.sub(with_, self))

    def replace_leading_non_word_characters(
            self,
            *,
            with_: str | 'String' = ' '
    ) -> String:
        """
        Replaces all leading non-word characters with the specified replacement string up to the first word character
        """
        return String(MATCH_LEADING_NON_WORD_CHARACTERS_REGEX.sub(with_, self))

    def replace_trailing_non_word_characters(
            self,
            *,
            with_: str | 'String' = ''
    ) -> String:
        """
        Replaces all trailing non-word characters with the specified replacement string from the last word character
        """
        return String(MATCH_TRAILING_NON_WORD_CHARACTERS_REGEX.sub(with_, self))

    def replace_trailing_words(
            self,
            *words: str,
            with_: str | 'String' = '',
    ) -> String:
        """
        Replace all trailing words with the specified replacement string.
        """
        pattern: re.Pattern = RegexUtil.get_compiled_re_with_joined_tokens(
            r'(\b{}\s?$)',
            r'\s?$|\b',
            *words
        )
        return String(pattern.sub(with_, self))

    def replace_words(self, *words: str | 'String', with_: str | 'String' = '', ignore_case: bool = False) -> String:
        """
        Replace all specified words with the specified replacement string.
        """
        regex: re.Pattern = RegexUtil.get_compiled_re_with_joined_tokens(
            r'^|\b{}\b|$',
            r"\b|\b",
            *words,
            flags=re.IGNORECASE if ignore_case else 0,
        )

        return String(regex.sub(with_, self))

    # ========================================================================================== SEARCH
    def index_of(self, substring: str | 'String', after_occurrences: int) -> int:
        """
        Returns the index of *substring* in *full_string* after *after_occurrences* occurrences.

        Exception-safe, will return -1 if not found.
        """
        index: int = 0
        for i in range(after_occurrences + 1):
            try:
                index = self.index(substring, index) + 1
            except ValueError:
                return -1

        return index

    # ========================================================================================== TRANSFORMATION
    def to_camel_case_strip_spaces(self) -> String:
        return String(string_casing.to_camel_case_strip_spaces(self))

    def to_camel_case_with_underscores(self) -> String:
        return String(string_casing.to_camel_case_with_underscores(self))

    def to_pascal_case_strip_spaces(self) -> String:
        return String(string_casing.to_pascal_case_strip_spaces(self))

    def to_pascal_case_with_underscores(self) -> String:
        return String(string_casing.to_pascal_case_with_underscores(self))

    def to_upper_case_with_underscores(self) -> String:
        return String(string_casing.to_upper_case_with_underscores(self))

    def transliterate_to_ascii(self) -> String:
        return String(standard_transliterate(self))

    # ======================================================================================== TRUNCATE
    def limit_string_length(self, length: int) -> str:
        return String(f"%.{length}s" % self)  # noqa


    # ========================================================================================== IS
    def is_float(self) -> bool:
        """
        Checks if *input_string* is a float number (returns True also when *input_string* is an integer).
        """
        # doc-src: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
        return self.replace(".", "", 1).isdigit()

    def tess(self) -> str:
        import inspect
        return inspect.currentframe().f_back.f_lineno


if __name__ == '__main__':
    print(String('roger').rreplace('ger'))