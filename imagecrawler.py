import base64
import sys
from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler
from six.moves.urllib.parse import urlparse
import argparse

import csv
from datetime import datetime
class MyImageDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg',# 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # works for python3
        filename = base64.b64encode(url_path.encode()).decode()
        return '{}_{}.{}'.format(args.search, datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f'), extension)


def main():

    if not args.search or not args.root_dir:
        a.print_help()
        sys.exit(1)


    google_crawler = GoogleImageCrawler(
        downloader_cls=MyImageDownloader,
        downloader_threads=4,
        storage={'root_dir': args.root_dir})
    google_crawler.crawl(args.search, max_num=args.nr)
    '''
    with open("cartoon.csv", 'r') as f:
        reader = csv.reader(f)
        print(reader)
        for row in reader:
            print(row)
            google_crawler.crawl(row[0], max_num=args.nr)
    '''

if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument("--search", help="search keyword")
    a.add_argument("--nr", help="number of queries", default=10)
    a.add_argument("--root_dir", help="root_dir")
    args = a.parse_args()
    args.nr = int(args.nr)
    main()