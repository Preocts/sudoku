from __future__ import annotations

from collections.abc import Sequence


class Cell:
    """A W by H sized cell of the board."""

    def __init__(
        self,
        *,
        width: int = 3,
        height: int = 3,
        valid_values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9},
        initial_values: Sequence[int | None] | None = None,
    ):
        """
        Initializes the cell as empty.

        Args:
            width (int): Width of the cell, default: 3
            height (int): Height of the cell, default: 3
            valid_valies (set[int]): Allowed unique values. Must equal the product of
                height and width.
            initial_values (Sequence[int | None]): Initial values of the cell. Provided
                left to right, top to bottom. If provided, must equal the product of
                heigh and width.

        Raises:
            ValueError: On validation errors of any provided values.
        """
        self._width = width
        self._height = height
        self._valid_values = valid_values
        self._cell_len = self._width * self._height

        if len(self._valid_values) != self._cell_len:
            msg = f"Valid values do not match cell size. Expected {self._cell_len} values, given {len(valid_values)} values."
            raise ValueError(msg)

        if initial_values is None:
            values: list[int | None] = [None] * self._cell_len

        else:
            values = list(initial_values)

            if len(values) != self._cell_len:
                msg = f"Cell defined as {self._width}x{self._height}. Expected {self._cell_len} initial values, given {len(values)} values."
                raise ValueError(msg)

        self._values = values

    @property
    def values(self) -> tuple[int | None, ...]:
        return tuple(self._values)

    def get_row(self, row_number: int) -> Sequence[int]:
        """
        Get a given horizontal row of a cell.

        Args:
            row_number (int): The row to be returned

        Returns:
            Sequence: The values of the row
        """
        return (0, 0, 0)
