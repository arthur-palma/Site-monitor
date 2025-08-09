import json
import interface as ui

def load(file_path):
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        ui.file_error()
        return []

def save(file_content, path):
    with open(path,"w") as file:
        json.dump(file_content,file,indent=4)

def add_content(content, path):
    file = load(path)
    file.append(content)
    save(file, path)