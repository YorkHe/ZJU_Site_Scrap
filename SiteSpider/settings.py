# -*- coding: utf-8 -*-

# Scrapy settings for SiteSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'SiteSpider'

SPIDER_MODULES = ['SiteSpider.spiders']
NEWSPIDER_MODULE = 'SiteSpider.spiders'
DEPTH_LIMIT = 5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SiteSpider (+http://www.yourdomain.com)'
