from SaveProvider import SaveProvider
from GrabbedItemLists import GrabbedItemLists
import requests
import datetime

class ItemsListGrabber:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def create_grab(self):
        currentTime = datetime.datetime.utcnow().isoformat(sep=" ", timespec="seconds")
        headers = {'Content-Type': 'text/html',}
        response = requests.get(self.url, headers=headers)
        raw_html = response.text
        return GrabbedItemLists(self.name, currentTime, raw_html, SaveProvider)

    def restore(self):
        loaded = SaveProvider.loadAll(self.name)
        return [GrabbedItemLists(self.name, l[0], l[1], SaveProvider) for l in loaded]