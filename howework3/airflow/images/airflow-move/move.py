import os
import shutil

import click

INPUT_FILES = ["data.csv", "targets.csv"]


@click.command("move-data")
@click.option("--input-dir")
@click.option("--output-dir")
def move(input_dir: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    for filename in INPUT_FILES:
        try:
            source = os.path.join(input_dir, filename)
            dest = os.path.join(output_dir, filename)
            shutil.copy(source, dest)
        except:
            pass


if __name__ == '__main__':
    predict()
