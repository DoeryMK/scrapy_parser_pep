import datetime as dt
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

now = dt.datetime.now()
now_formatted = now.strftime(DATETIME_FORMAT)

LOGS = 'logs'
LOG_DIR = BASE_DIR / LOGS
LOG_FILE = LOG_DIR / 'parser.logs'
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOG_LEVEL = 'DEBUG'
LOG_FILE_APPEND = True

FILE_FORMAT = 'csv'

SUMMARY_NAME = 'status_summary'
SUMMARY_FILE_NAME = f'{SUMMARY_NAME}_{now_formatted}.{FILE_FORMAT}'
SUMMARY_TABLE_HEADER = ('Status', 'Quantity')
SUMMARY_TABLE_BOTTOM = 'Total'

PEP_NAME = 'pep'
PEP_FILE_NAME = f'{PEP_NAME}_%(time)s.{FILE_FORMAT}'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
