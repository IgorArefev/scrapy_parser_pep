from pathlib import Path

BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
BASE_DIR = Path(__file__).parent.parent
FILENAME = 'status_summary_{}.csv'
RESULTS_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
PATTERN = r'PEP\s(?P<number>\d+)[\s–]+(?P<name>.+)$'
