from typing import Dict

from nomad.config import config
from nomad.datamodel import EntryArchive
from nomad.parsing.parser import MatchingParser

configuration = config.get_plugin_entry_point('nomad_{{cookiecutter.module_name}}.parsers:myparser')


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: Dict[str, EntryArchive] = None,
    ) -> None:
        logger.info(f'MyParser.parse: parameter={configuration.parameter}')
        archive.data.name = 'Value from parser'
