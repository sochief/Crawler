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
    queue = project_name + '/queue.txt'
    #list of the waiting list to be crawled
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        #does the queue.txt is exist already?
        write_file(queue,base_url)
        #we give the crawler the base url to start from
    if not os.path.isfile(crawled):
        write_file(crawled,'')



# Create a new file
def write_file(path,data):
    f = open(path,'w')#We give a path and 'w' means write,creating a file
    f.write(data)#giving a data for it
    f.close()


# Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:#'a' stays for append, so it will add links to the end of the file
        file.write(data + '\n')





# Delete the contents of the file
def delete_file_contents(path):
    with open(path,'w'):
        pass #keyword to do nothing



# Bad thing anout using variables! If the computer shuts off, or there is a bug, all the data is going to be lost
# With files, all of the data is going to be saved, but it will take more time



# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f: #'rt' means read text file
        for line in f:
            results.add(line.replace('\n','')) #add a line to a set, and there is a new line character(line 33)
    return results #return the set, looking good

# Iterate through a set, each item will be a new line in the file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(link):
        append_to_file(file,link)
