from urllib.request import urlopen #allows us to connect to pages to PY
from link_finder import LinkFinder
from general import *

class Spider:

# Class variables (shared )
# We creare a class variable so we can share the data among its own instances
#These are class variables (shared among all instances)
    project_name =' '
#homepage url
    base_url = ''
    domain_name = ''
    queue_file ='' # text file
    crawled_file = ''
    queue = set() # waiting list
    crawled = set() # all of the pages are crawled
    # queue_file and queue are going to have the same data in it, we dont want to write into a file every single link we have
    # files are stored on the harddrive, and the last two variables are stored in the RAM
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        # so every spider shares the same info
        self.boot()
        self.crawl_page('First spider', Spider.base_url)
    
    @staticmethod
    def boot(self):
        # So we give a first thread to create a project directory and queue.txt and crawled.txt files
            create_project_dir(Spider.project_name)
            create_data_files(Spider.project_name, Spider.base_url)
            Spider.queue = file_to_set(Spider.queue_file)
            Spider.crawled =file_to_set(Spider.crawled_file)
    

    @staticmethod
    def crawl_page(tread_name, page_url):
        if page_url not in Spider.crawled:
            print(tread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + '| Crawled: ' +str(len(Spider.crawled)) )
            Spider.add_links_to_queue(Spider.gather_link(page_url)) #connect to a webpage and return a set of links that it found on the webpage
            # once we have it, we add it to the list, so all of the threads can see that
            Spider.queue.remove(page_url)# remove the page, we just crawled
            Spider.crawled.add(page_url)# so we move it from the waiting list to the crawled list
            # So the ones up care about the sets, not the files, which we need to update as well 
            Spider.update_files()
    @staticmethod
    def gather_links(page_url):   # connects to a site, takes a html, converts it to a proper string html format and passes it to a link finder
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                #make sure that we are connecting to an actual web-page
                html_bytes = response.read()#those ones are just ones and zeroes
                html_string = html_bytes.decode("utf-8")#which we can actually pass to a link finder, which parses through it, gets a set of all of the link in it, and if there are no issues, it gives it back to ya
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            # if it is not a link, or the site booted us off
            print('Error: cannot crawl page ')
            return set()# just return an empty set
        return finder.page_links()
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url: # not to crawl the whole internet
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)        


