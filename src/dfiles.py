import os
from utils.links import *
from utils.drivefiles import *

def drivehosted(url) 
    command = "wget --no-check-certificate "+url    
    os.system(command)
    return os.cwd()

def download_drive(url):
    elinks=crawl(url)
    for link in elinks:
        drivehosted(parse_url(link))