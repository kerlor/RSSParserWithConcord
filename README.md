# RSSParserWithConcord
RSSFeedGenerator and RSSFeedParser are computation files to be use with concord.io framework. 

RSSFeedGenerator is responsible for crawling http://www.craigslist.org/about/best/all/index[0-5000+].rss 
and filtering for url+summary then send it over to RSSFeedParser. 

RSSFeedParser searches the summary for "free" string then sends the url to the logger. It is not much of a parser, 
but it demonstrates how to use the streaming framework.

See http://docs.concord.io/ for detail on creating computation file for Concord. 


