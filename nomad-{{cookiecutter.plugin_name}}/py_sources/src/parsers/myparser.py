from nomad.config import config
from nomad.datamodel import EntryArchive
from nomad.datamodel.results import Material, Results
from nomad.parsing.parser import MatchingParser

configuration = config.get_plugin_entry_point('nomad_{{cookiecutter.module_name}}.parsers:myparser')


class MyParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: dict[str, EntryArchive] = None,
    ) -> None:
        logger.info(f'MyParser.parse: parameter={configuration.parameter}')
        archive.results = Results(material=Material(elements=['H', 'O']))
