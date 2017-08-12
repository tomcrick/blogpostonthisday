import time
from datetime import date
from calendar import monthrange
from scrapy.spiders import CrawlSpider

class OnThisDaySpider(CrawlSpider):
    name = "onthisday_spider"
    allowed_domains = ["proftomcrick.com"]

    # URL string with format specifiers
    url_string = ("http://proftomcrick.com/{year}/{month}/")

    # create a list of start urls to crawl formatting the string above
    # so that correct month end dates are used i.e. 28 for February
    # on non-leap years
    start_urls = []
    today = date.today()
    startyear = 2011
    nextyear = today.year + 1
    
    for year in range(startyear, nextyear):
        start_urls.append(url_string.format(year=year, month=today.month))
