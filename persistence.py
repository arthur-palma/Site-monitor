import json
import interface as ui
path = "site_urls.json"

def load_urls():
    try:
        with open(path,"r") as urls:
            return json.load(urls)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        ui.file_error()
        return []
    
def save_urls(urls):
    with open(path,"w") as file:
        json.dump(urls,file,indent=4)

def add_url(url):
    urls = load_urls()
    urls.append(url)
    save_urls(urls)
