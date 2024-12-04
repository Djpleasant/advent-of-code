#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""https://adventofcode.com/2024/day/2"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import (
    NamedTuple,
    Sequence,
)

# ----------#
# Globals #
# ----------#
INPUT_DATA_FILE = Path("static/day_02")


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


def parse_input_data_row(row: str) -> Sequence[int]:
    # Sanitize and split row into int items.
    split_row = row.strip().split()

    # Cast row items to int and put in a tuple.
    processed_row = [int(num) for num in split_row]

    # Return row of ints.
    return tuple(processed_row)


def read_input_data(file: Path) -> None:
    # Define reports container.
    all_reports = []

    # Get file contents.
    with file.open("r", encoding="utf-8") as f:
        data_lines = f.readlines()

    # Create lists from the input data.
    for line in data_lines:
        reports = parse_input_data_row(row=line)
        all_reports.append(reports)

    # Return lists.
    return tuple(all_reports)


def report_is_good(report: Sequence[int]) -> bool:
    report_trending_direction = None
    report_has_failed_once = False
    for i in range(len(report)):
        # Break when the last item is the current level.
        if i == (len(report) - 1):
            break

        # Get levels to compare.
        current_level = report[i]
        next_level = report[i + 1]

        # Get the variance between this level and the next level.
        level_variance = abs(current_level - next_level)

        # Get the trend direction between this level and the next level.
        # (True means increasing.)
        level_trend = current_level < next_level

        # Check for level variance.
        if not (1 <= level_variance <= 3):
            return False

        # Catch first trend observation since a change can't be determined yet.
        if report_trending_direction is None:
            report_trending_direction = level_trend
            continue

        # Check for trend change.
        if report_trending_direction != level_trend:
            return False

    return True


def get_number_of_good_reports(reports):
    good_reports_count = 0
    for report in reports:
        if report_is_good(report=report):
            good_reports_count += 1
    return good_reports_count


# -------#
# Main #
# -------#
async def aentrypoint(args: Sequence[str]) -> int:
    """Script entrypoint function."""
    # Get processed cli arguments.
    cli = parse_cli_arguments(args=args)

    # Get lists.
    reports = read_input_data(cli.input_data_file)

    # Determine the amount of good reports.
    good_reports_count = get_number_of_good_reports(reports=reports)

    # Build data to output.
    output = {
        "good_reports": good_reports_count,
    }

    # Print list to stdout and return success.
    print(json.dumps(output), file=sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(aentrypoint(sys.argv)))
