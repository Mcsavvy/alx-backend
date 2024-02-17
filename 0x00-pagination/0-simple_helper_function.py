#!/usr/bin/env python3
"""index range generator."""

from typing import Tuple


def index_range(page: int, page_size) -> Tuple[int, int]:
    """Generate an index range.

    Args:
        page: the current page
        page_size: the number of items in every page.
    """
    return (
        ((page - 1) * page_size),
        (page * page_size)
    )
