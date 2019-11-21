import os
# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)
        #it will create directory, if it doesn't exists
        #the crawler will work simultaniosly with lots of theards
#Create queue and crawled files (if not created)
def create_data_files(project_name,base_url):
    queue = project_name + 'queue.txt'
    #list of the waiting list to be crawled
    crawled = project_name + 'crawled.txt'
    if not os.path.isfile(queue):
        #does the queue.txt is exist already?
        write_file(queue,base_url)
        #we give the crawler the base url to start from
    if not os.path.isfile(crawled):
        write.file(crawled,'')








# Create a new file
def write_file(path,data):
    f = open(path,'w')#We give a path and 'w' means write,creating a file
    f.write(data)#giving a data for it
    f.close()