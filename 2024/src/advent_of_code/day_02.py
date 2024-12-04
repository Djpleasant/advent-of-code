#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""https://adventofcode.com/2024/day/2

- https://github.com/maread99/aoc/blob/main/2024/02.py
    - This was a helpful reference when I got stuck with
      part two.
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import (
    NamedTuple,
    Mapping,
)
import itertools

# ----------#
# Globals #
# ----------#
INPUT_DATA_FILE = Path("static/day_02")

LEVEL_MIN_VARIANCE = 1
LEVEL_MAX_VARIANCE = 3

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


def _parse_input_data_row(row: str) -> list[int]:
    # Sanitize and split row into int items.
    split_row = row.strip().split()

    # Cast row items to int and put in a tuple.
    processed_row = [int(num) for num in split_row]

    # Return row of ints.
    return list(processed_row)


def _read_input_data(file: Path) -> None:
    # Define reports container.
    all_reports = []

    # Get file contents.
    with file.open("r", encoding="utf-8") as f:
        data_lines = f.readlines()

    # Create lists from the input data.
    for line in data_lines:
        reports = _parse_input_data_row(row=line)
        all_reports.append(reports)

    # Return lists.
    return list(all_reports)

def _get_report_with_level_removed(
    report: list[int], level_index: int
) -> list[int]:
    filtered_report = report.copy()
    del filtered_report[level_index]
    return filtered_report

def _get_level_step_observations(level: int, next_level: int) -> tuple[int, bool]:
    level_variance = abs(level - next_level)
    level_trend = next_level > level
    return (level_variance, level_trend)

def _report_passes_draconian_standards(report: list[int]) -> bool:
    report_trending_direction: bool = None
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

def _report_passes_regular_standards(report: list[int]) -> bool|int:
    # Set the report trend based on the first two elements.
    report_trend = report[1] > report[0]
    for level, next_level in itertools.pairwise(report):
        variance, trend = _get_level_step_observations(
            level=level,
            next_level=next_level,
        )
        # Check for consistent trend.
        if report_trend != trend:
            return False

        # Check for in-bounds variance.
        if not (LEVEL_MIN_VARIANCE <= variance <= LEVEL_MAX_VARIANCE):
            return False
    return True

def do_part_one(reports: list[list[int]]) -> int:
    good_reports_count = 0
    for report in reports:
        if _report_passes_draconian_standards(report=report):
            good_reports_count += 1
    return good_reports_count


def do_part_two(reports: list[list[int]]) -> int:
    good_reports_count = 0
    for report in reports:
        report_is_safe = _report_passes_regular_standards(report=report)
        if not report_is_safe:
            for i in range(len(report)):
                _report = report.copy()
                del _report[i]
                report_is_safe = _report_passes_regular_standards(report=_report)
                if report_is_safe:
                    break
        if report_is_safe:
            good_reports_count += 1
        else:
            pass
    return good_reports_count


# -------#
# Main #
# -------#
async def aentrypoint(args: list[str]) -> int:
    """Script entrypoint function."""
    # Get processed cli arguments.
    cli = _parse_cli_arguments(args=args)

    # Get lists.
    reports = _read_input_data(cli.input_data_file)

    # Determine the amount of good reports.
    good_reports_by_draconian_standards = do_part_one(reports=reports)
    good_reports_by_regular_standards = do_part_two(reports=reports)

    # Build data to output.
    output: Mapping[str, int] = {
        "part_one": good_reports_by_draconian_standards,
        "part_two": good_reports_by_regular_standards,
    }

    # Print list to stdout and return success.
    print(json.dumps(output), file=sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(aentrypoint(sys.argv)))
