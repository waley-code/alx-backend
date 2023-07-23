#!/usr/bin/env python3
"""takes two integer arguments page and page_size"""

import csv
from typing import List

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
