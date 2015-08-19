import sys
import time
import concord
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

class RSSParser(Computation):
    def __init__(self):
        pass

    def init(self, ctx):
        self.count=1
        logger.info("Source initialized")

    def process_record(self, ctx, record):
        j=json.loads(record.data)
        if j['summary'].find('free') != -1:
            logger.info("Someone is giving away free stuff! url =" +j['url'])
        #logger.info("receiving = "+record.data)
        self.count+=1
        #logger.info("threads parsed:"+str(self.count))

    def metadata(self):
        return Metadata(
            name='rssfeedparser',
            istreams=['rssfeeds'],
            ostreams=[])

logger.info("Main")
serve_computation(RSSParser())
