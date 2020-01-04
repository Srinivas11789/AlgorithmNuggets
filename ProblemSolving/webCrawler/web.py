# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        
        # Logic 1: Backtrack and Recurse --> 23 % faster 100 pass
        def back_track_crawl(start, parser, valid):
            crawled = parser.getUrls(start)
            for url in crawled:
                if self.domain in url and url not in valid:
                    valid.add(url)
                    back_track_crawl(url, parser, valid)
            return valid
        
        self.domain = startUrl.strip("https://")
        self.domain = self.domain.split("/")[0]
        return back_track_crawl(startUrl, htmlParser, {startUrl})
