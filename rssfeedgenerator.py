import sys
import time
import concord
import feedparser
import json
from concord.computation import (
    Computation,
    Metadata,
    serve_computation
)

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def time_millis():
    return int(round(time.time() * 1000))

class RSSGenerator(Computation):
    def __init__(self):
        self.url = "http://www.craigslist.org/about/best/all/index"
        self.index=0
        self.count=1
    def init(self, ctx):
        logger.info("Source initialized")
        ctx.set_timer('loop', time_millis())

    def process_timer(self, ctx, key, time):
        completeurl  = self.url+str(self.index)+".rss"
        self.index+=25
        logger.info("sending content from "+completeurl)

        d = feedparser.parse( completeurl )
        for a in d['entries']:
            #logger.info("reading from rss obj")
            summary =a['summary_detail']['value']
            link=a['links'][0]['href']
            #logger.info("creatign json data")
            data = {}
            data['url'] = link
            data['summary']=summary
            json_data = json.dumps(data)
            #logger.info("created json data")
            ctx.produce_record("rssfeeds", "content", json_data.encode('utf-8'))
            #logger.info("sent message")
            self.count+=1
        #logger.info("sent "+str(self.count)+" items")
        ctx.set_timer('loop', time_millis() + 1000)


    def process_record(self, ctx, record):
        raise Exception('process_record not implemented')

    def metadata(self):
        return Metadata(
            name='rssfeedgenerator',
            istreams=[],
            ostreams=['rssfeeds'])

logger.info("Main")
serve_computation(RSSGenerator())
