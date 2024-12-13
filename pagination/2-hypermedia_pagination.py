#!/usr/bin/env python3
"""Server class to paginate a dataset with hypermedia links."""
import csv
from typing import List, Dict
from math import ceil
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a page of data with hypermedia links."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()

        # If the page exceeds the total data length, return an empty list.
        if start >= len(data):
            return {}

        # Paginate data.
        page_data = data[start:end]

        # Calculate total number of pages.
        total_pages = ceil(len(data) / page_size)

        # Construct hypermedia links.
        links = {}
        if page > 1:
            links["prev"] = f"/page/{page - 1}?page_size={page_size}"
        if page < total_pages:
            links["next"] = f"/page/{page + 1}?page_size={page_size}"

        return {
            "page": page,
            "page_size": page_size,
            "data": page_data,
            "links": links
        }

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary with hypermedia information."""
        # Use get_page to fetch the data and other relevant info
        page_data = self.get_page(page, page_size)

        # If no data returned, handle it gracefully
        if not page_data:
            return {
                "page_size": page_size,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": 0,
            }

        # Calculate total number of pages.
        total_pages = ceil(len(self.dataset()) / page_size)

        # Check for next and previous page.
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": page_data["data"],
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
