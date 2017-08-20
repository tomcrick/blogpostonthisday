# -*- coding: utf-8 -*-
import dateutil.parser
from datetime import date
from collections import defaultdict
from scrapy.spiders import CrawlSpider

class OnThisDaySpider(CrawlSpider):
    # spider info
    name = "onthisday_spider"
    allowed_domains = ["proftomcrick.com"]

    # URL string with format specifiers
    url_string = ("http://proftomcrick.com/{year}/{month}/")

    # create a list of start URLs to crawl over the entire blog history using current month
    start_urls = []
    today = date.today()
    startyear = 2011
    nextyear = today.year + 1

    for year in range(startyear, nextyear):
        start_urls.append(url_string.format(year=year, month=today.month))

    # grab info on individual blog posts from this month's summary page
    def parse(self, response):

        #onthisday = defaultdict(list)
        POST_SELECTOR = '.entry-header'
        for post in response.css(POST_SELECTOR):

            TITLE_SELECTOR = 'h1 ::text'
            URL_SELECTOR = 'a::attr(href)'
            DATE_SELECTOR = './/a/time/@datetime'

            #title = post.css(TITLE_SELECTOR).extract_first()
            #url = post.css(URL_SELECTOR).extract_first()
            #date = dateutil.parser.parse((post.xpath(DATE_SELECTOR).extract_first()))

            # return post details
            #if date.day == date.today().day:

            yield{
                #onthisday[date].append([title,url])
                'title': post.css(TITLE_SELECTOR).extract_first(),
                'url': post.css(URL_SELECTOR).extract_first(),
                'date': dateutil.parser.parse((post.xpath(DATE_SELECTOR).extract_first())),
            }

                #print(title)
                #print(url)
                #print(date)
