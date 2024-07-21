#!/usr/bin/env python3
'''
function named index_range that takes
two integer arguments page and page_size
'''
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    return a tuple of size two containing a start index and an end index
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        '''
        takes two integer arguments page with default
        value 1 and page_size with default value 10
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        takes two integer arguments page with default
        value 1 and page_size with default value 10
        '''
        page_data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
