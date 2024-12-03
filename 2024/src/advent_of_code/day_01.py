#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""entrypoint for AoC 2024 - Day 01."""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import (
    NamedTuple,
    Sequence,
)

# ----------#
# Globals #
# ----------#
INPUT_DATA_FILE = Path("static/day_01")


class CliArguments(NamedTuple):
    input_data_file: Path


# ------------#
# Functions #
# ------------#
def validate_cli_aruguments(cli: CliArguments):
    """Run validation checks on cli arguments."""
    # Verify file exists.
    if not cli.input_data_file.exists():
        raise FileNotFoundError(
            "Could not find the data file.", cli.input_data_file
        )

    # Indicate success.
    return True


def parse_cli_arguments(args: list[str]) -> CliArguments:
    """Creates a parser to consume the arguments provided to the script."""
    # Create parser.
    parser = argparse.ArgumentParser(
        prog=__file__,
        description="Aoc 2024 - Day 01.",
    )

    # Add cli arguments.
    parser.add_argument(
        "-i",
        "--input-data-file",
        type=Path,
        default=INPUT_DATA_FILE,
        help="Build context for the container build runtime.",
    )

    # Pull defined flags out of provided cli arguments.
    args, _ = parser.parse_known_args(args=args)

    # Return parsed cli arguments.
    return args


def parse_input_data_row(row: str) -> tuple[int, int]:
    # Define return items.
    list_one_item: int = None
    list_two_item: int = None

    # Sanitize and split list into.
    split_row = row.strip().split()

    # Cast list items to numeric.
    list_one_item = int(split_row[0])
    list_two_item = int(split_row[1])

    # Return parsed items.
    return (list_one_item, list_two_item)


def read_input_data(file: Path) -> tuple[Sequence[int], Sequence[int]]:
    # Define lists.
    list_one: Sequence[int] = []
    list_two: Sequence[int] = []

    # Get file contents.
    with file.open("r", encoding="utf-8") as f:
        data_lines = f.readlines()

    for line in data_lines:
        list_one_item, list_two_item = parse_input_data_row(row=line)
        list_one.append(list_one_item)
        list_two.append(list_two_item)

    # Return lists.
    return (tuple(list_one), tuple(list_two))


# -------#
# Main #
# -------#
async def aentrypoint(args: Sequence[str]) -> int:
    """Script entrypoint function."""
    # Get processed cli arguments.
    cli = parse_cli_arguments(args=args)

    # Get lists.
    list_one, list_two = read_input_data(cli.input_data_file)

    print(f"List one has {len(list_one)} item(s) in it.")
    print(f"List one has {len(list_two)} item(s) in it.")

    # Indicate success.
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(aentrypoint(sys.argv)))
