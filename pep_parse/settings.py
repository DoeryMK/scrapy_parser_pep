from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOGS = 'logs'
LOG_DIR = BASE_DIR / LOGS
LOG_FILE = LOG_DIR / 'parser.logs'
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOG_LEVEL = 'DEBUG'
LOG_FILE_APPEND = True

SUMMARY_FILE_NAME = 'status_summary'
SUMMARY_TABLE_HEADER = ('Status', 'Quantity')
SUMMARY_TABLE_BOTTOM = 'Total'

CSV_FILE_FORMAT = 'csv'

PEP = 'pep'
PEP_FILE_NAME = f'{PEP}_%(time)s.csv'

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': CSV_FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
