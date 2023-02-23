import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, RESULTS, SUMMARY_FILE_NAME,
                                SUMMARY_TABLE_BOTTOM, SUMMARY_TABLE_HEADER)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def close_spider(self, spider):
        file_path = self.results_dir / SUMMARY_FILE_NAME
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows([
                SUMMARY_TABLE_HEADER,
                *self.statuses.items(),
                (SUMMARY_TABLE_BOTTOM, sum(self.statuses.values())),
            ])

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item
