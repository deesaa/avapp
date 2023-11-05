import datetime
import os
import jsonpickle

from GrabbedItemLists import GrabbedItemLists
from ItemRaw import ItemRaw

class ItemsPageRawSaver:
    def save(object : GrabbedItemLists):
        path = f"data/{object.origin_name}/{object.date}/saved_page.json"
        dir_name = os.path.dirname(path)
        os.makedirs(dir_name, exist_ok=True)
        json_str = jsonpickle.encode(object)
        with open(path, "w") as save_file:
            save_file.write(json_str)
        pass
    
class ItemRawSaver:
    def save(object : ItemRaw):
        
        bad_chars = [';', ':', '!', "*", "\\", '/', "@", "#"]
        item_file_name = ''.join((filter(lambda i: i not in bad_chars, object.item_head.title)))
        path = f"data/{object.item_head.grab_group.origin_name}/{object.item_head.grab_group.date}/items_raw/{item_file_name}.json"
        dir_name = os.path.dirname(path)
        os.makedirs(dir_name, exist_ok=True)
        json_str = jsonpickle.encode(object)
        with open(path, "w") as save_file:
            save_file.write(json_str)
        pass

class SaveProvider:
    
    savers = {GrabbedItemLists : ItemsPageRawSaver, 
              ItemRaw : ItemRawSaver}
    
    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False, sort_keys=True, indent=4)
    
    def save(object):
        SaveProvider.savers[type(object)].save(object)
        
    def loadAll(origin_name):
        if not os.path.isdir(f"data/{origin_name}"):
            print(f"NO SAVE DATA FOR {origin_name}")
            pass

        fileNames = [f for f in os.listdir(f"data/{origin_name}") if os.path.isfile(f"data/{origin_name}/{f}")]
        files = [SaveProvider.open_file(origin_name, f) for f in fileNames]
        return files

    def open_file(origin_name, file_name):
        date_string = os.path.splitext(file_name)[0]
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        with open(f"data/{origin_name}/{file_name}") as file:
            return (date, file.read())