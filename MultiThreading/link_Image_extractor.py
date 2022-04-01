from urllib.request import urlopen, urljoin
from builtwith import builtwith
import re

def download_page(url):
    return urlopen(url).read().decode('utf-8')
def extract_links(page): #a / href --> img / src
    link_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    return link_regex.findall(page)


if __name__ == '__main__':
    target_url = ''
    apress = download_page(target_url)
    links = extract_links(apress)
    for link in links:
        print(urljoin(target_url, link))
    print(builtwith(target_url))