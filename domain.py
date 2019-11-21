from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]# returns the last two elements of the domain
    except:
        return ''



# We only care about domain
# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

