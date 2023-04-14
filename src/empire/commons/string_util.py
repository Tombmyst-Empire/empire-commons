import random
import string
from functools import lru_cache


class StringUtil:
    """
    Utility methods for strings

    **DEPRECATED: use empire_string instead**
    """

    @staticmethod
    def rreplace(
        input_string: str, replacee: str, replacement: str, count: int = 1
    ) -> str:
        """
        Replaces starting from the right of string.

        .. note:: This method is useful only for replacing *replacee* by *replacement*, not for removing *replacee*.
        """
        # src: https://stackoverflow.com/questions/9943504/right-to-left-string-replace-in-python
        return replacement.join(input_string.rsplit(replacee, count))

    @staticmethod
    def contains_any_of(input_string: str, *what: str, case_sensitive: bool = True) -> bool:
        """
        Returns True if *the_string* contains any of *what*.
        """
        # doc-src: https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
        if not case_sensitive:
            input_string = input_string.lower()

        return any(item in input_string for item in what)

    @staticmethod
    def is_float(input_string: str) -> bool:
        """
        Checks if *input_string* is a float number (returns True also when *input_string* is an integer).
        """
        # doc-src: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
        return input_string.replace(".", "", 1).isdigit()

    @staticmethod
    def generate_random_string(string_length: int, *, lowercase: bool = False) -> str:
        """
        Generates a random string of length *string_length*.
        """
        random_string: str = "".join(
            random.choice(string.ascii_uppercase) for _ in range(string_length)
        )

        return random_string.lower() if lowercase else random_string

    @staticmethod
    def batch_replace(input_string: str, *replacees: str, replacement: str = "") -> str:
        """
        Replaces all occurrences of *replacees* to *replacement* in *input_string*
        """
        for replacee in replacees:
            input_string = input_string.replace(replacee, replacement)

        return input_string

    @staticmethod
    def join_non_nulls_non_empty(
        strings: list[str], separator: str
    ) -> str:  # TODO: improve
        result: str = ""
        for s in strings:
            if s:
                result += s + separator

        return result[0 : -len(separator)]

    @staticmethod
    def limit_string_length(full_string: str, length: int) -> str:
        return f"%.{length}s" % full_string

    @staticmethod
    def to_camel_case(text: str) -> str:
        """
        Returns a camelCase version of *text*.
        """
        camel_case: str = StringUtil.to_pascal_case(text)
        return camel_case[0].lower() + camel_case[1:]

    @staticmethod
    def to_pascal_case(text: str) -> str:
        """
        Returns a PascalCase version of *text*.
        """
        if not text:
            return text

        words: list[str] = text.replace("-", " ").replace("_", " ").split()
        return "".join(word.capitalize() for word in words)

    @staticmethod
    @lru_cache(maxsize=256)
    def tokenize_string_to_words(full_string: str) -> list[str]:
        return full_string.split()

    @staticmethod
    def index_of(full_string: str, substring: str, after_occurrences: int) -> int:
        """
        Returns the index of *substring* in *full_string* after *after_occurrences* occurrences.

        Exception-safe, will return -1 if not found.
        """
        index: int = 0
        for i in range(after_occurrences + 1):
            try:
                index = full_string.index(substring, index) + 1
            except ValueError:
                return -1

        return index

    @staticmethod
    def times(string: str, amount: int) -> str:
        """
        Returns *string* * *amount*.

        If *amount* < 0, amount will be set to 0
        """
        if amount < 0:
            amount = 0
            
        return string * amount
