# goes through the html code and takes up all of the links
from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
# In html parser there is a method called handlestartag
    def handle_starttag(self, tag, attrs):
        if tag == 'a':#a tag means its a link
            for (attribute,value) in attrs:#a href -- is an attrubute, link is a value
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)
    def page_links(self):
        return self.links
                # we only look for the href attribute, the other stuff doesn't matter
    def error(self, message):
        pass


# finder = linkFinder()# we make an object which is an html parser, then we call a function called feed
# We create a link finder obj and we are gonna feed it in with html page
# Once it gets all of the links right here (handle_starttag), we call page_links function