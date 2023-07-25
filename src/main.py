"""
Script to fix Facebook data archive emoji encoding
See https://sorashi.github.io/fix-facebook-json-archive-encoding/ for more detail
"""

from pathlib import Path
import re
import click


@click.command()
@click.argument(
    "source",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
)
@click.argument(
    "destination",
    type=click.Path(exists=False, file_okay=False, path_type=Path),
)
@click.option(
    "--file-glob",
    type=str,
    default="**/*.json",
    show_default=True,
    help="The glob pattern used to select the files that will be processed",
)
def main(source: Path, destination: Path, file_glob: str):
    """
    Fix the encoding of JSON data from Facebook data requests.

    SOURCE:         The directory that contains the raw data files.

    DESTINATION:    The directory where amended data will be created.
    """
    file_paths = list(source.glob(file_glob))
    with click.progressbar(file_paths, label="Processing files") as progress_bar:
        for source_file_path in progress_bar:
            destination_file_path = destination.joinpath(
                source_file_path.relative_to(source)
            )
            with open(source_file_path, encoding="utf-8") as source_file:
                file_content = source_file.read()
            replaced = re.sub(
                r"\\u00([a-f0-9]{2})",
                lambda x: chr(int(x.group(1), 16)),
                file_content,
            )
            buffer = [ord(c) for c in replaced]
            result = bytes(buffer).decode("utf-8")
            destination_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(
                destination_file_path, encoding="utf-8", mode="w"
            ) as destination_file:
                destination_file.write(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
