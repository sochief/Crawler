# Allows PY to connect to pages
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

# We creare a class variable
# So we can share the data among it's own instances
# These are class variables (shared among all instances)
    project_name =' '
# Homepage url
    base_url = ''
    domain_name = ''
    # Text files
    queue_file =''
    crawled_file = ''
    # Waiting list
    queue = set()
    crawled = set() # All of the pages are crawled
    # queue_file and queue are going to have the same data in it
    # we dont want to write into a file every single link we have
    # files are stored on the harddrive
    # and the last two variables are stored in the RAM
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        # So every spider has the same info
        self.boot()
        self.crawl_page('First spider', Spider.base_url)
    @staticmethod
    def boot(self):
        # We give a first thread to create a project directory
        # and queue.txt and crawled.txt files
            create_project_dir(Spider.project_name)
            create_data_files(Spider.project_name, Spider.base_url)
            Spider.queue = file_to_set(Spider.queue_file)
            Spider.crawled =file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(tread_name, page_url):
        if page_url not in Spider.crawled:
            print(tread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + '| Crawled: ' +str(len(Spider.crawled)) )
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            # Connect to a webpage
            # and return a set of links that it found on the webpage
            # once we have it, we add it to the list, so all of the threads can see that
            # Remove the page we just crawled
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            # So we move it from the waiting list to the crawled list
            # The ones up care about the sets,
            # not the files, which we need to update as well
            Spider.update_files()
    @staticmethod
    def gather_links(page_url):
        # 1) Connects to a site
        # 2) Takes a html
        # 3) Converts it to a proper string html format
        # 4) Passes it to a link finder
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                # Make sure that we are connecting to an actual web-page
                html_bytes = response.read()
                # Those ones are just ones and zeroes
                html_string = html_bytes.decode("utf-8")
                # Which we pass to a link finder
                # Which parses through it
                # Gets a set of all of the link in it
                # And if there are no issues, it gives it back to ya
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            # If it is not a link, or if the site booted us off
            print('Error: cannot crawl page ')
            return set()
            # Just return an empty set
        return finder.page_links()
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                # Not to crawl the whole internet,just go through the domain name
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)


