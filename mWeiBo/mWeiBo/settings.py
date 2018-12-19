# -*- coding: utf-8 -*-

# Scrapy settings for mWeiBo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mWeiBo'

SPIDER_MODULES = ['mWeiBo.spiders']
NEWSPIDER_MODULE = 'mWeiBo.spiders'

#my settings
cookies={'SINAGLOBAL': '4755601353474.194.1541510261825', ' ULV': '1545115501654:15:7:2:3200853564029.704.1545115501631:1545095612684', ' SUHB': '0cSnj9DYyv7N4B', ' UOR': ',,club.huawei.com', ' SCF': 'AtEk8FBQy4HGGWry3yoR0Dpy7nnRkuXxdYPJ0-aRrcpxcczcTJ9D2dXrnBvURdk4tJCEfhlxciASOmZo6UPCw_Y.', ' SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWUhrLSOmm3bM-0pZMKiyEK5JpX5oz75NHD95QfSo.Xe0BcSK.fWs4DqcjUi--fi-z7iKysi--fi-2Xi-zXi--4iK.EiKnRws7t', ' ALF': '1547743534', ' un': '15323768477', ' wvr': '6', ' SUB': '_2A25xHVR-DeRhGeNI4lYS9CjJwjmIHXVS_nw2rDV8PUJbkNAKLWPXkW1NSAIjQVkCp4eIU61TVp3acb2wGsH2KvGv', ' SSOLoginState': '1545115499', ' _s_tentry': '-', ' Apache': '3200853564029.704.1545115501631'}
UA='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

MONGO_URI = 'localhost'

MONGO_DATABASE = 'weibo'

COOKIES_URL = 'http://localhost:5000/weibo/random'

PROXY_URL = 'http://localhost:5555/random'

# RETRY_HTTP_CODES = [401, 403, 408, 414, 500, 502, 503, 504]

ITEM_PIPELINES = {
    'mWeiBo.pipelines.TimePipeline': 300,
    'mWeiBo.pipelines.MweiboPipeline': 301,
    'mWeiBo.pipelines.MongoPipeline': 302,
}

DOWNLOADER_MIDDLEWARES = {
    'mWeiBo.middlewares.CookiesMiddleware': 554,
    'mWeiBo.middlewares.ProxyMiddleware': 555,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mWeiBo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'mWeiBo.middlewares.MweiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'mWeiBo.middlewares.MweiboDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'mWeiBo.pipelines.MweiboPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
