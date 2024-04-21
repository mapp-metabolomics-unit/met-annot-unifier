# met-annot-unifier

[![Release](https://img.shields.io/github/v/release/mapp-metabolomics-unit/met-annot-unifier)](https://img.shields.io/github/v/release/mapp-metabolomics-unit/met-annot-unifier)
[![Build status](https://img.shields.io/github/actions/workflow/status/mapp-metabolomics-unit/met-annot-unifier/main.yml?branch=main)](https://github.com/mapp-metabolomics-unit/met-annot-unifier/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/mapp-metabolomics-unit/met-annot-unifier/branch/main/graph/badge.svg)](https://codecov.io/gh/mapp-metabolomics-unit/met-annot-unifier)
[![Commit activity](https://img.shields.io/github/commit-activity/m/mapp-metabolomics-unit/met-annot-unifier)](https://img.shields.io/github/commit-activity/m/mapp-metabolomics-unit/met-annot-unifier)
[![License](https://img.shields.io/github/license/mapp-metabolomics-unit/met-annot-unifier)](https://img.shields.io/github/license/mapp-metabolomics-unit/met-annot-unifier)

A Python project to combine tabular outputs from GNPS, Sirius and ISDB

- **Github repository**: <https://github.com/mapp-metabolomics-unit/met-annot-unifier/>
- **Documentation** <https://mapp-metabolomics-unit.github.io/met-annot-unifier/>

## Quickstart

### Installation

met-annot-unifier is available on PyPi and can be installed with pip:

```bash
pip install met-annot-unifier
```

### Usage

For now the package is only available as a command line tool. You can run it with the following command:

```bash
python -m met_annot_unifier.cli
```

Get help on the available modes with:

```bash
python -m met_annot_unifier.cli --help
```

#### Examples

You can align the annotations tables from GNPS, Sirius and ISDB using two modes:

- `align-horizontally`: This will return a long table with a single row for each unique compound (according to their planar structures or IK2D). This mode can be useful to output a table to be viewed in [Datawarrior](https://openmolecules.org/datawarrior/) or similar tools for chemical structures exploration.

```bash
python -m met_annot_unifier.cli align-horizontally --gnps-file <path-to-gnps-table> --sirius-file <path-to-sirius-table> --isdb-file <path-to-isdb-table> --output <output-path>
```

- `align-vertically`: This will return a wide table with a single row per feature (m/z and retention time) and columns for each of the three sources. This mode can be useful to output a table to be added to a molecular network to be visualized in [Cytoscape](https://cytoscape.org/) or similar tools for network visualization.

```bash
python -m met_annot_unifier.cli align-vertically --gnps-file <path-to-gnps-table> --sirius-file <path-to-sirius-table> --isdb-file <path-to-isdb-table> --output <output-path>
```

You can find example tables in the `examples/data` folder of this repository. So from the root of this repository you can run the following command to align the tables horizontally:

```bash
python -m met_annot_unifier.cli align-horizontally --gnps-file examples/data/gnps_output_example.tsv --sirius-file examples/data/sirius_output_example.tsv --isdb-file examples/data/isdb_output_example.tsv --output examples/data/aligned_table_horizontally.csv
```

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
