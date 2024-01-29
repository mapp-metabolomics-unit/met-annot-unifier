import click


@click.command()
@click.option("--gnps-file", type=click.Path(exists=True), help="Path to GNPS output file.")
@click.option("--sirius-file", type=click.Path(exists=True), help="Path to Sirius output file.")
@click.option("--isdb-file", type=click.Path(exists=True), help="Path to ISDB output file.")
def main(gnps_file, sirius_file, isdb_file):
    """CLI tool to align metabolite annotations from GNPS, Sirius, and ISDB."""
    click.echo("Aligning metabolite annotations...")
    # Call the function to handle the alignment logic


if __name__ == "__main__":
    main()
