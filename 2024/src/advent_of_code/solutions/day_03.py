#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""https://adventofcode.com/2024/day/3"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import (
    NamedTuple,
    Mapping,
)
import re

from advent_of_code.utils import read_input_data

# ----------#
# Globals #
# ----------#
SOLUTION_NAME = "AoC 2024 - Day 03"

INPUT_DATA_FILE = Path("static/day_03")

PART_ONE_REGEX_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"
PART_TWO_REGEX_PATTERN = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))"

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

def calculate_matched_expression(expression: str) -> int:
    # Strip 'mul(' from the expression.
    expression = expression[4:]

    # Strip ')' from the expression.
    expression = expression[:-1]

    # Parse ints from remaining expression.
    nums = expression.split(',')
    first = int(nums[0])
    second = int(nums[1])
    
    # Calculate expression and return value.
    calc = first * second
    return calc

# -------#
# Main #
# -------#
def do_part_one(input_data: list[str]) -> int:
    total = 0
    for line in input_data:
        matches = re.findall(pattern=PART_ONE_REGEX_PATTERN, string=line)
        for match in matches:
            calc = calculate_matched_expression(expression=match)
            total+=calc
    return total


def do_part_two(input_data: list[str]) -> int:
    total = 0
    calculate_enabled: bool = True
    for line in input_data:
        matches: list[str] = re.findall(pattern=PART_TWO_REGEX_PATTERN, string=line)
        for match in matches:
            if match == "do()":
                calculate_enabled = True
                continue
            elif match == "don't()":
                calculate_enabled = False
                continue

            if calculate_enabled:
                calc = calculate_matched_expression(expression=match)
                total+=calc
    return total


async def aentrypoint(args: list[str]) -> int:
    """Script entrypoint function."""
    # Get processed cli arguments.
    cli = _parse_cli_arguments(args=args)

    # Read in input data.
    input_data = read_input_data(cli.input_data_file)

    # Get results from worker functions.
    part_one_result = do_part_one(input_data=input_data)
    part_two_result = do_part_two(input_data=input_data)

    # Build data to output.
    output: Mapping[str, int] = {
        "part_one": part_one_result,
        "part_two": part_two_result,
    }

    # Print list to stdout and return success.
    print(json.dumps(output), file=sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(aentrypoint(sys.argv)))
