import logging
from typing import Callable


def main(program_name: str, program_version: str, program_headline: str, function: Callable, *args, **kwargs):
    logging.info('%s v.%s', program_name, program_version)
    logging.info('*** %s ***', program_headline)
    function(*args, **kwargs)


def async_main(program_name: str, program_version: str, program_headline: str, function: Callable, *args, **kwargs):
    import asyncio
    logging.info('%s v.%s', program_name, program_version)
    logging.info('*** %s ***', program_headline)
    asyncio.run(function(*args, **kwargs))
