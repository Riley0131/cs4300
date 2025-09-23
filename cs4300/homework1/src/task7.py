import requests

def get(site):
    response = requests.get(site)
    
    #return the status code
    return response.status_code