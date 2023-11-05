from doctest import Example
import time
from ItemRaw import ItemRaw
from ItemHead import ItemHead
from GrabbedItemLists import GrabbedItemLists
import requests
import datetime
from SaveProvider import SaveProvider
import numpy

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
        headers = {'Content-Type': 'text/html', 'User-Agent': 'Mozilla/5.0'}
        response = requests.get(item_full_url, headers=headers)
        self.url_delay()
        raw_html = response.text
        
        self.throw_if_ip_denied(raw_html, self.name+f"->{item_head.title}"+"->create_item_from_head")
        print(f"Completed: " + self.name+f"->{item_head.title}"+"->create_item_from_head")
        return ItemRaw(item_head, raw_html, SaveProvider)
        pass
    
    def throw_if_ip_denied(self, raw_html, log_text):
        if "Доступ ограничен" in raw_html:
            raise DeniedIpException(log_text)
        
    def url_delay(self):
        time.sleep(numpy.random.normal(3, 1))

    def create_grab(self):
        currentTime = datetime.datetime.utcnow().isoformat(sep=" ", timespec="seconds")
        headers = {'Content-Type': 'text/html',}
        response = requests.get(self.url, headers=headers)
        self.url_delay()
        raw_html = response.text
        
        self.throw_if_ip_denied(raw_html, self.name+"->create_grab")
        print(f"Completed: " + self.name+"->create_grab")
        return GrabbedItemLists(self.name, currentTime, raw_html, SaveProvider)

    def restore(self):
        loaded = SaveProvider.loadAll(self.name)
        return [GrabbedItemLists(self.name, l[0], l[1], SaveProvider) for l in loaded]
    
    def restore_items(self):
        loaded = SaveProvider.load_all_items(self.name)
        return [ItemRaw(ItemHead('', '', ''))]
    
    
    
class DeniedIpException(Exception):
    def __init__(self, log_text, *args: object) -> None:
        super().__init__(*args)
        self.log_text = log_text