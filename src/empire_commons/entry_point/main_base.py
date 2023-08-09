import asyncio
import argparse
from typing import Any, Optional

from empire_commons.functions import dummy_that_returns_first_arg, to_closure
from empire_commons.entry_point.argument import Argument
import ereport


LOGGER = ereport.get_or_make_reporter('COMMONS', 'E_COMMONS_LOGGING_LEVEL')


class Main:
    """
    Base main program sequence.
    """
    __slots__ = (
        'program_name',
        'program_version',
        'program_headline',
        'args',
        '_receives_args',
        '_args_load_closure'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        *,
        receives_args: bool = False
    ):
        self.program_name: str = program_name
        self.program_version: str = program_version
        self.program_headline: str = program_headline
        self.args: dict[str, Any] = {}

        self._receives_args: bool = receives_args
        self._args_load_closure = to_closure(dummy_that_returns_first_arg, True)

    def start(self, *args, **kwargs):
        (
            self.preinit(*args, **kwargs) &
            self._args_load_closure() &
            self.init(self.args, *args, **kwargs) &
            self.load(self.args, *args, **kwargs) &
            self.postinit(self.args, *args, **kwargs) &
            self.main(self.args, *args, **kwargs) &
            self.presave(self.args, *args, **kwargs) &
            self.save(self.args, *args, **kwargs) &
            self.postsave(self.args, *args, **kwargs)
        )
        self.end(self.args, *args, **kwargs)

    def preinit(self, *args, **kwargs) -> bool:
        """
        Pre-Init event.
        Override if needed and call super().preinit()
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.info('%s v.%s', self.program_name, self.program_version)
        LOGGER.info('*** %s ***', self.program_headline)
        return True

    def args_load(
        self,
        description: Optional[str] = None,
        *arguments: Argument
    ):
        """
        Specify program args, if necessary
        :param description: Description provided to argparse instance
        :param arguments: Arguments
        """
        def _closure():
            if not self._receives_args:
                return

            parser = argparse.ArgumentParser(
                prog=self.program_name,
                description=description
            )

            for argument in arguments:
                parser.add_argument(
                    *argument.name_or_flags,
                    action=argument.action.value(),
                    nargs=argument.nargs,
                    consts=argument.const,
                    default=argument.default,
                    type=argument.type,
                    choices=argument.choices,
                    required=argument.required,
                    help=argument.help,
                    metavar=argument.metavar,
                    dest=argument.dest
                )

            parsed = parser.parse_args()
            self.args = vars(parsed)
            return True

        self._args_load_closure = _closure

    def init(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Init event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Init seq.')
        return True

    def load(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Load event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Load seq.')
        return True

    def postinit(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Postinit event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Postinit seq.')
        return True

    def main(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Main event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Main seq.')
        return True

    def presave(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Presave event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Presave seq.')
        return True

    def save(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Save event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Save seq.')
        return True

    def postsave(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Postsave event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Postsave seq.')
        return True

    def end(self, parsed_args: dict[str, Any], *args, **kwargs):
        """
        End event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        """
        LOGGER.trace('End seq.')


class AsyncMain:
    """
    Base main program sequence.
    """
    __slots__ = (
        'program_name',
        'program_version',
        'program_headline',
        'args',
        '_receives_args',
        '_args_load_closure'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        *,
        receives_args: bool = False
    ):
        self.program_name: str = program_name
        self.program_version: str = program_version
        self.program_headline: str = program_headline
        self.args: dict[str, Any] = {}

        self._receives_args: bool = receives_args
        self._args_load_closure = to_closure(dummy_that_returns_first_arg, True)

    def start(self, *args, **kwargs):
        asyncio.run(self._start(*args, **kwargs))

    async def _start(self, *args, **kwargs):
        (
            await self.preinit(*args, **kwargs) &
            self._args_load_closure() &
            await self.init(self.args, *args, **kwargs) &
            await self.load(self.args, *args, **kwargs) &
            await self.postinit(self.args, *args, **kwargs) &
            await self.main(self.args, *args, **kwargs) &
            await self.presave(self.args, *args, **kwargs) &
            await self.save(self.args, *args, **kwargs) &
            await self.postsave(self.args, *args, **kwargs)
        )
        await self.end(self.args, *args, **kwargs)

    async def preinit(self, *args, **kwargs) -> bool:
        """
        Pre-Init event.
        Override if needed and call super().preinit()
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.info('%s v.%s', self.program_name, self.program_version)
        LOGGER.info('*** %s ***', self.program_headline)
        return True

    def args_load(
        self,
        description: Optional[str] = None,
        *arguments: Argument
    ):
        """
        Specify program args, if necessary
        :param description: Description provided to argparse instance
        :param arguments: Arguments
        """
        def _closure():
            if not self._receives_args:
                return

            parser = argparse.ArgumentParser(
                prog=self.program_name,
                description=description
            )

            for argument in arguments:
                parser.add_argument(
                    *argument.name_or_flags,
                    action=argument.action.value(),
                    nargs=argument.nargs,
                    consts=argument.const,
                    default=argument.default,
                    type=argument.type,
                    choices=argument.choices,
                    required=argument.required,
                    help=argument.help,
                    metavar=argument.metavar,
                    dest=argument.dest
                )

            parsed = parser.parse_args()
            self.args = vars(parsed)
            return True

        self._args_load_closure = _closure

    async def init(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Init event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Init seq.')
        return True

    async def load(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Load event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Load seq.')
        return True

    async def postinit(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Postinit event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Postinit seq.')
        return True

    async def main(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Main event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Main seq.')
        return True

    async def presave(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Presave event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Presave seq.')
        return True

    async def save(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Save event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Save seq.')
        return True

    async def postsave(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        """
        Postsave event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        :return: Return True to continue execution, false to halt
        """
        LOGGER.trace('Postsave seq.')
        return True

    async def end(self, parsed_args: dict[str, Any], *args, **kwargs):
        """
        End event
        :param parsed_args: Parsed args, if any
        :param args:
        :param kwargs:
        """
        LOGGER.trace('End seq.')
