#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""https://adventofcode.com/2024/day/1"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import (
    NamedTuple,
)

from advent_of_code.utils import (
    read_input_data,
)

# ----------#
# Globals #
# ----------#
SOLUTION_NAME = "AoC 2024 - Day 01"

INPUT_DATA_FILE = Path("static/day_01")


class CliArguments(NamedTuple):
    input_data_file: Path


# ------------#
# Functions #
# ------------#
def _validate_cli_aruguments(cli: CliArguments):
    """Run validation checks on cli arguments."""
    # Verify file exists.
    if not cli.input_data_file.exists():
        raise FileNotFoundError(
            "Could not find the data file.", cli.input_data_file
        )

    # Indicate success.
    return True


def _parse_cli_arguments(args: list[str]) -> CliArguments:
    """Creates a parser to consume the arguments provided to the script."""
    # Create parser.
    parser = argparse.ArgumentParser(
        prog=__file__,
        description=SOLUTION_NAME,
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


def _parse_input_data_row(row: str) -> tuple[int, int]:
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


def _parse_lists_from_input_data(
    input_data: list[str],
) -> tuple[list[int], list[int]]:
    # Define separate lists.
    list_one: list[int] = []
    list_two: list[int] = []

    for row in input_data:
        list_one_item, list_two_item = _parse_input_data_row(row=row)
        list_one.append(list_one_item)
        list_two.append(list_two_item)

    return (list_one, list_two)


def _pop_smallest_number(numbers: list[int]) -> tuple[int, list[int]]:
    # Get max int size so the first element is guaranteed to be smaller.
    min_number = sys.maxsize
    min_index = -1

    # Loop over list and get the smallest number and its index.
    for i, num in enumerate(numbers):
        if num < min_number:
            min_number = num
            min_index = i

    # Copy the list but ignore smallest number.
    trimmed_list = [numbers[i] for i in range(len(numbers)) if i != min_index]

    # Return the smallest number and the original list without that number.
    return (min_number, trimmed_list)


# -------#
# Main #
# -------#
def do_part_one(input_data: list[str]) -> int:
    # Deserialize lists data.
    list_one, list_two = _parse_lists_from_input_data(input_data=input_data)

    # Calculate distance between reports.
    total_distance = 0
    for _ in range(len(list_one)):
        list_one_smallest, list_one = _pop_smallest_number(numbers=list_one)
        list_two_smallest, list_two = _pop_smallest_number(numbers=list_two)
        if list_one_smallest != list_two_smallest:
            total_distance += abs(list_one_smallest - list_two_smallest)

    # Return calculation.
    return total_distance


def do_part_two(input_data: list[str]) -> int:
    # Deserialize lists data.
    list_one, list_two = _parse_lists_from_input_data(input_data=input_data)

    # Generate a map of unique list two numbers and how often they occur.
    list_two_hash = {}
    for num in list_two:
        if num in list_two_hash.keys():
            list_two_hash[num] = list_two_hash[num] + 1
        else:
            list_two_hash[num] = 1

    # Define score to add to.
    simularity_score = 0

    # If the list one item appears in list two, multiply itself by the number
    # of instances found in list two, then add that to the total.
    for num in list_one:
        if num in list_two_hash.keys():
            simularity_score += num * list_two_hash[num]

    # Return calculation.
    return simularity_score


async def aentrypoint(args: list[str]) -> int:
    """Script entrypoint function."""
    # Get processed cli arguments.
    cli = _parse_cli_arguments(args=args)

    # Read in input data.
    input_data = read_input_data(cli.input_data_file)

    # Determine the amount of good reports.
    part_one_result = do_part_one(input_data=input_data)
    part_two_result = do_part_two(input_data=input_data)

    # Build data to output.
    output: dict[str, int] = {
        "part_one": part_one_result,
        "part_two": part_two_result,
    }

    # Print output to stdout and return success.
    print(json.dumps(output), file=sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(aentrypoint(sys.argv)))
