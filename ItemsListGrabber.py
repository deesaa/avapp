from ItemRaw import ItemRaw
from ItemHead import ItemHead
from GrabbedItemLists import GrabbedItemLists
import requests
import datetime
from SaveProvider import SaveProvider

class TitleExcluder:
    def __init__(self, exclude_title : set) -> None:
        self.exclude_title = [str(x).lower() for x in exclude_title]
    
    def is_exclude(self, item_head : ItemHead): 
        title_lower = item_head.title.lower()
        is_in = any(title in title_lower for title in self.exclude_title)
        return is_in

class ItemsListGrabber:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        
    def add_excluder(self, title_exclude_config):
        self.title_exclude = TitleExcluder(title_exclude_config)
        
    def is_exclude_item_head(self, item_head : ItemHead):
        if(hasattr(self, "title_exclude")):
            return self.title_exclude.is_exclude(item_head)
        
    def create_item_from_head(self, item_head : ItemHead) -> ItemRaw:
        item_url = item_head.url
        item_full_url = "https://avito.ru" + item_url
        headers = {'Content-Type': 'text/html',}
        response = requests.get(item_full_url, headers=headers)
        raw_html = response.text
        return ItemRaw(item_head, raw_html, SaveProvider)
        pass
            

    def create_grab(self):
        currentTime = datetime.datetime.utcnow().isoformat(sep=" ", timespec="seconds")
        headers = {'Content-Type': 'text/html',}
        response = requests.get(self.url, headers=headers)
        raw_html = response.text
        return GrabbedItemLists(self.name, currentTime, raw_html, SaveProvider)

    def restore(self):
        loaded = SaveProvider.loadAll(self.name)
        return [GrabbedItemLists(self.name, l[0], l[1], SaveProvider) for l in loaded]