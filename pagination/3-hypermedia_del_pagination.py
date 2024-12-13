#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a hypermedia pagination"""

        assert isinstance(index, int) and index >= 0, "Index must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.indexed_dataset()

        # Initialize variables
        data = []
        current_index = index
        remaining_size = page_size

        # Loop to collect data for the current page, skipping deleted items
        while remaining_size > 0 and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                remaining_size -= 1
            current_index += 1

        # Calculate the next index and handle out-of-range cases
        next_index = current_index if remaining_size == 0 else None
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
