#!/usr/bin/env python3
"""Implement a simple pagination."""


import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize server."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data.

        Args:
            page (int, optional): the page to display. Defaults to 1.
            page_size (int, optional): the size of the page. Defaults to 10.

        Returns:
            List[List]: data from the database
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, stop = index_range(page, page_size)
        return self.dataset()[start:stop]
