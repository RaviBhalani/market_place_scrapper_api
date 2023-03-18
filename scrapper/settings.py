"""
Scrapping Settings Start.
"""

AMAZON_INDIA_URL = 'https://www.amazon.in/'
AMAZON_US_URL = 'https://www.amazon.com/'

WEBSITE_URL = AMAZON_INDIA_URL
PRODUCT_URL_KEY = 's?k='
WEBSITE_PAGE_KEY = '&page='
LANGUAGE = 'en-US'
PARSER = 'lxml'

USER_AGENT_LIST = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) '
    'Version/13.1.1 Safari/605.1.15',

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/83.0.4103.97 Safari/537.36',

    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

"""
Scrapping Settings End.
"""