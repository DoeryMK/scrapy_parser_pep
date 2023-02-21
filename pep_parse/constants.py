from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RESULTS = 'results'
RESULTS_DIR = BASE_DIR.parent / RESULTS


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'


LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'parser.logs'

SUMMARY_FILE_NAME = 'status_summary'
SUMMARY_TABLE_HEADER = ('Статус', 'Количество')
SUMMARY_TABLE_BOTTOM = 'Total'
