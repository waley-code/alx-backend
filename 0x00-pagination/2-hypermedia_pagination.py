#!/usr/bin/env python3
"""takes two integer arguments page and page_size"""

import csv
import math
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    """ Calculate the start and end
        indexes for a given pagination
    """
    if page <= 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Verify that page and page_size are integers greater than 0"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        try:
            start_index, end_index = index_range(page, page_size)
            re: list = self.dataset()
            return re[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Range of the page

            Args:
                page: Current page
                page_size: Total size of the page

            Return:
                Dict with different arguments
                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                (equivalent to return from previous task)
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page,
                None if no previous page
                total_pages: the total number of pages
                in the dataset as an integer
        """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        totalpag: int = len(dataset) if dataset else 0
        totalpag = math.ceil(totalpag / page_size)
        prevpag: int = (page - 1) if (page - 1) >= 1 else None
        nextpag: int = (page + 1) if (page + 1) <= totalpag else None

        hypermedia: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextpag,
            'prev_page': prevpag,
            'total_pages': totalpag,
        }

        return hypermedia
