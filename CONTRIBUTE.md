## Checks

```bash
make check
```

```bash
pre-commit run --all-files
```

## Commands

Run the cli as follows:

```bash
poetry run met-annot-unifier-cli --help
```

```bash
poetry run met-annot-unifier-cli --gnps-file tests/data/gnps_output_example.tsv --sirius-file tests/data/sirius_output_example.tsv --isdb-file tests/data/isdb_output_example.tsv --output tests/data/output.tsv
```
