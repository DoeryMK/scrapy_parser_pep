from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR.parent / RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

LOGS = 'logs'
LOG_DIR = BASE_DIR / LOGS
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'parser.logs'
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOG_LEVEL = 'DEBUG'

SUMMARY_FILE_NAME = 'status_summary'
SUMMARY_TABLE_HEADER = ('Status', 'Quantity')
SUMMARY_TABLE_BOTTOM = 'Total'

CSV_FILE_FORMAT = 'csv'

PEP = 'pep'
PEP_FILE_NAME = f'{PEP}_%(time)s.csv'
PEP_TABLE_HEADER = ['number', 'name', 'status']

FEEDS = {
    f'{RESULTS}/{PEP_FILE_NAME}': {
        'format': CSV_FILE_FORMAT,
        'fields': PEP_TABLE_HEADER,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
