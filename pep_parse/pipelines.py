import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (BASE_DIR, DATETIME_FORMAT, RESULTS,
                                 SUMMARY_FILE_NAME, SUMMARY_TABLE_BOTTOM,
                                 SUMMARY_TABLE_HEADER)


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses_dict = defaultdict(int)

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'{SUMMARY_FILE_NAME}_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect
            ).writerows([
                SUMMARY_TABLE_HEADER,
                *self.statuses_dict.items(),
                (SUMMARY_TABLE_BOTTOM, sum(self.statuses_dict.values())),
            ])

    def process_item(self, item, spider):
        self.statuses_dict[item.get('status')] += 1
        return item
