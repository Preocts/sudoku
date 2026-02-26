from __future__ import annotations

import pytest

from sudoku.cell import Cell


def test_default_init() -> None:
    """Test the defaults for a Cell."""
    expected_len = 9
    expected_values = tuple([None] * expected_len)

    cell = Cell()

    assert len(cell.values) == expected_len
    assert cell.values == expected_values


def test_customize_initial_values() -> None:
    """Custom initial values are used."""
    expected_values = (1, 2, 3, 4, None, 6, 7, 8, 9)

    cell = Cell(initial_values=expected_values)

    assert cell.values == expected_values


def test_valid_values_much_match_size() -> None:
    """Raise if the provided valid values do not match the given size."""
    match = "Valid values do not match cell size. Expected 16 values, given 9 values."

    with pytest.raises(ValueError, match=match):
        Cell(width=4, height=4)


def test_initial_values_much_match_size() -> None:
    """Raise if the provided initial values do not match the given size."""
    initial_values = [1, 2, 3, 4, 5, 6, 7, 8]
    match = "Cell defined as 3x3. Expected 9 initial values, given 8 values."

    with pytest.raises(ValueError, match=match):
        Cell(initial_values=initial_values)


def test_initial_values_are_validated() -> None:
    """Raise if provided intitial values violate valid values."""
    initial_values = [1, 2, 3, 4, 5, 6, 7, 8, 8]
    match = "Provided initial values are not a valid cell arrangement."

    with pytest.raises(ValueError, match=match):
        Cell(initial_values=initial_values)
