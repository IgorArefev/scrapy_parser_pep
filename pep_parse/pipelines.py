import csv
from collections import defaultdict
from datetime import datetime as dt
from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, FILENAME, RESULTS_DIR, TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = defaultdict(int)

    def process_item(self, item, spider):
        if 'status' not in item:
            raise DropItem('Статус не найден')
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.time = dt.now().strftime(TIME_FORMAT)
        results_dir = BASE_DIR / RESULTS_DIR
        file_path = results_dir / FILENAME.format(self.time)
        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            self.counter['Total'] = sum(self.counter.values())
            writer.writerows(self.counter.items())
