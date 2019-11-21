import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# Implement this in GUI
PROJECT_NAME = 'PUT YOUR NAME'
# Do this in GUI as well
HOMEPAGE = 'PUT A NAME HERE'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
# Depends on operating system and RAM
NUMBER_OF_THREADS = 8
queue = Queue()
# When a program just starts, we cant go to the multithreading
# Because it needs to create files and directories
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # to be sure that it dies, when the main exits
        t.start()

# Do the next job in the queue
def work():
    while True:
        # Get the next item
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name,url)
        queue.task_done()



# Each queued link is a new job

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, and if so, it's gonna crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()