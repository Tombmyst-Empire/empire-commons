"""
Module for RegexUtil class.
"""

import re

import regex
from functools import lru_cache


class RegexUtil:
    """
    Utility class for regexes.
    """
    _re_cache: dict[tuple[str, str], re.Pattern] = {}
    _regex_cache: dict[tuple[str, str], regex.Pattern] = {}

    @staticmethod
    @lru_cache(maxsize=4096)
    def get_compiled_re(pattern: str, flags: int = 0) -> re.Pattern:
        """
        Compiles a given regex pattern.

        The method caches every given pattern. It has utility when compiling dynamic patterns on the fly.
        """
        return re.compile(pattern, flags)

    @staticmethod
    @lru_cache(maxsize=4096)
    def get_compiled_re_with_joined_tokens(pattern: str, joining_token: str, *tokens: str, flags: int = 0) -> re.Pattern:
        """
        Builds and compile *pattern* by joining *tokens* with *joining_token*. In order to properly work,
        *pattern* should contain a single ``{}`` placeholder that will be replaced by joined tokens using format().

        The method caches every given pattern. It has utility when compiling dynamic patterns on the fly.
        """
        return re.compile(pattern.format(joining_token.join([re.escape(token) for token in tokens])), flags=flags)

    @staticmethod
    @lru_cache(maxsize=4096)
    def get_compiled_regex(pattern: str, flags: int = 0) -> regex.Pattern:
        """
        Compiles a given regex pattern using regex library instead of builtin.

        The method caches every given pattern. It has utility when compiling dynamic patterns on the fly.
        """
        return regex.compile(pattern, flags)
