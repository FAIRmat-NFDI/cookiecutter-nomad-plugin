#!/usr/bin/env python3
"""
Created on Fri Sep 27 09:08:03 2024

@author: a2853
"""

#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pandas as pd
from baseclasses.helper.solar_cell_batch_mapping import (
    get_reference,
    map_atomic_layer_deposition,
    map_basic_sample,
    map_batch,
    map_cleaning,
    map_evaporation,
    map_generic,
    map_inkjet_printing,
    map_laser_scribing,
    map_sdc,
    map_spin_coating,
    map_sputtering,
    map_substrate,
)
from baseclasses.helper.utilities import create_archive
from nomad.datamodel import EntryArchive
from nomad.datamodel.data import EntryData
from nomad.datamodel.metainfo.basesections import Entity
from nomad.metainfo import Quantity
from nomad.parsing import MatchingParser

from {{cookiecutter.module_name}}.parsers.file_parser.ink_recycling_mappers import map_ink_recycling
from {{cookiecutter.module_name}}.schema_packages.{{cookiecutter.lab_name}}_package import (
    {{cookiecutter.lab_name}}_Batch,
    {{cookiecutter.lab_name}}_Cleaning,
    {{cookiecutter.lab_name}}_Evaporation,
    {{cookiecutter.lab_name}}_Inkjet_Printing,
    {{cookiecutter.lab_name}}_LaserScribing,
    {{cookiecutter.lab_name}}_Process,
    {{cookiecutter.lab_name}}_Sample,
    {{cookiecutter.lab_name}}_SlotDieCoating,
    {{cookiecutter.lab_name}}_SpinCoating,
    {{cookiecutter.lab_name}}_Sputtering,
    {{cookiecutter.lab_name}}_Substrate,
    IRIS_AtomicLayerDeposition,
    ProcessParameter,
)
from {{cookiecutter.module_name}}.schema_packages.ink_recycling_package import (
    InkRecycling_RecyclingExperiment,  # Added back this import
)

"""
This is a hello world style example for an example parser/converter.
"""


class Raw{{cookiecutter.lab_name}}Experiment(EntryData):
    processed_archive = Quantity(type=Entity, shape=['*'])


def map_generic_parameters(process, data):
    parameters = []
    for col, val in data.items():
        if col in ['Notes', 'Name']:
            continue
        if pd.isna(val):
            continue
        try:
            val_float = float(val)
            parameters.append(ProcessParameter(name=col, value_number=val_float))
        except Exception:
            parameters.append(ProcessParameter(name=col, value_string=val))
    process.process_parameters = parameters


class {{cookiecutter.lab_name}}ExperimentParser(MatchingParser):
    def is_mainfile(
        self,
        filename: str,
        mime: str,
        buffer: bytes,
        decoded_buffer: str,
        compression: str = None,
    ):
        is_mainfile_super = super().is_mainfile(filename, mime, buffer, decoded_buffer, compression)
        if not is_mainfile_super:
            return False
        try:
            df = pd.read_excel(filename, header=[0, 1])
            df['Experiment Info']['Nomad ID'].dropna().to_list()
        except Exception:
            return False
        return True

    def parse(self, mainfile: str, archive: EntryArchive, logger):
        upload_id = archive.metadata.upload_id
        # xls = pd.ExcelFile(mainfile)
        df = pd.read_excel(mainfile, header=[0, 1])

        sample_ids = df['Experiment Info']['Nomad ID'].dropna().to_list()
        batch_id = '_'.join(sample_ids[0].split('_')[:-1])
        archives = [map_batch(sample_ids, batch_id, upload_id, {{cookiecutter.lab_name}}_Batch)]
        substrates = []
        substrates_col = [
            'Sample dimension',
            'Sample area [cm^2]',
            'Pixel area [cm^2]',
            'Number of pixels',
            'Notes',
            'Substrate material',
            'Substrate conductive layer',
        ]
        substrates_col = [s for s in substrates_col if s in df['Experiment Info'].columns]
        for i, sub in df['Experiment Info'][substrates_col].drop_duplicates().iterrows():
            if pd.isna(sub).all():
                continue
            substrates.append((f'{i}_substrate', sub, map_substrate(sub, {{cookiecutter.lab_name}}_Substrate)))

        def find_substrate(d):
            for s in substrates:
                if d.equals(s[1]):
                    return s[0]

        for i, row in df['Experiment Info'].iterrows():
            if pd.isna(row).all():
                continue
            substrate_name = find_substrate(row[substrates_col]) + '.archive.json' if substrates_col else None
            archives.append(map_basic_sample(row, substrate_name, upload_id, {{cookiecutter.lab_name}}_Sample))

        for i, col in enumerate(df.columns.get_level_values(0).unique()):
            if col == 'Experiment Info':
                continue

            df_dropped = df[col].drop_duplicates()
            for j, row in df_dropped.iterrows():
                if row.dropna().empty:
                    continue
                lab_ids = [
                    x['Experiment Info']['Nomad ID']
                    for _, x in df[['Experiment Info', col]].iterrows()
                    if x[col].astype('object').equals(row.astype('object'))
                ]
                if 'Cleaning' in col:
                    archives.append(map_cleaning(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_Cleaning))

                if 'Laser Scribing' in col:
                    archives.append(map_laser_scribing(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_LaserScribing))

                if 'Ink Recycling' in col:
                    archives.append(
                        map_ink_recycling(i, j, lab_ids, row, upload_id, InkRecycling_RecyclingExperiment)
                    )

                if 'Generic Process' in col:  # move up
                    generic_process = map_generic(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_Process)
                    map_generic_parameters(generic_process[1], row)
                    archives.append(generic_process)

                if pd.isna(row.get('Material name')):
                    continue

                if 'Evaporation' in col:
                    coevap = False
                    if 'Co-Evaporation' in col:
                        coevap = True
                    archives.append(
                        map_evaporation(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_Evaporation, coevap)
                    )

                if 'Spin Coating' in col:
                    archives.append(map_spin_coating(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_SpinCoating))

                if 'Slot Die Coating' in col:
                    archives.append(map_sdc(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_SlotDieCoating))

                if 'Sputtering' in col:
                    archives.append(map_sputtering(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_Sputtering))

                if 'Inkjet Printing' in col:
                    archives.append(
                        map_inkjet_printing(i, j, lab_ids, row, upload_id, {{cookiecutter.lab_name}}_Inkjet_Printing)
                    )

                if 'ALD' in col:
                    archives.append(
                        map_atomic_layer_deposition(i, j, lab_ids, row, upload_id, IRIS_AtomicLayerDeposition)
                    )

        refs = []
        for subs in substrates:
            file_name = f'{subs[0]}.archive.json'
            create_archive(subs[2], archive, file_name)
            refs.append(get_reference(upload_id, file_name))

        for a in archives:
            file_name = f'{a[0]}.archive.json'
            create_archive(a[1], archive, file_name)
            refs.append(get_reference(upload_id, file_name))

        archive.data = Raw{{cookiecutter.lab_name}}Experiment(processed_archive=refs)