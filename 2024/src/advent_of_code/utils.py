"""common utilities for the 2024 advent of code solutions."""

from pathlib import Path

# ----------#
# Globals #
# ----------#


# ------------#
# Functions #
# ------------#
def read_input_data(file: Path, encoding: str = "utf-8") -> tuple[str]:
    """Returns the utf-8 decoded lines from the provided file.

    Args:
        file (Path): File containing the static problem data for the day.
        encoding (str, optional): The encoding used for the input data.
        Defaults to "utf-8".

    Raises:
        FileNotFoundError: Raised if the provided file could not be found.

    Returns:
        tuple[str]: Iterable of the lines from the data input file.
    """
    # Define reports container.
    input_data_lines = []

    # Ensure file exists.
    if not file.exists():
        raise FileNotFoundError("Could not find data input file.", file)

    # Get file contents.
    with file.open("r", encoding=encoding) as f:
        data_lines = f.readlines()

    # Create lists from the input data.
    for line in data_lines:
        input_data_lines.append(line)

    # Return lists.
    return tuple(input_data_lines)
