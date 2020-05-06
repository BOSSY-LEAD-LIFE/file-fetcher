import os

def locallyhosted(url,dir) 
    command = "wget  -e robots=off  --accept '*.pdf'  --level=1  --recursive   -\"" + url +"\""     
    os.system(command)
    return os.cwd()
